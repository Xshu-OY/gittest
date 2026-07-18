# 导入时间模块，用于记录缓存块的访问时间
import time
# 导入抽象基类模块，用于定义抽象方法
from abc import ABC, abstractmethod

class CacheBlock:
    """缓存块，包含地址、顺序、最后访问时间和访问次数"""

    def __init__(self, address, order):
        """
        初始化缓存块，设置地址、顺序、时间和次数
        """
        self.addr = address      # 存储的地址
        self.order = order      # 进入缓存的顺序（用于FIFO）
        self.last_time = time.time()  # 最后访问时间（用于LRU）
        self.count = 1          # 访问次数（用于LFU），创建时为1
    
    
    def hit_update(self):
        """命中时更新时间和次数"""
        self.last_time = time.time()  # 更新最后访问时间
        self.count += 1                # 访问次数加1
    
    def __str__(self):
        return f"[{self.addr}]"  # 返回格式化字符串

class CachePolicy(ABC):
    """缓存策略基类"""
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.blocks = []
        self.hits = 0
        self.misses = 0
        self.next_order = 0
    
    def access(self, addr):
        """处理访问请求"""
        # 查找是否命中
        for block in self.blocks:
            if block.addr == addr:
                block.hit_update()
                self.hits += 1
                return True, None
        
        # 未命中
        self.misses += 1
        evicted = None
        
        if len(self.blocks) < self.capacity:
            # 缓存未满，直接添加
            self.next_order += 1
            self.blocks.append(CacheBlock(addr, self.next_order))
        else:
            # 缓存已满，需要替换
            idx = self._select_to_replace()
            evicted = self.blocks.pop(idx).addr
            self.next_order += 1
            self.blocks.append(CacheBlock(addr, self.next_order))
        
        return False, evicted
    
    @abstractmethod
    def _select_to_replace(self):
        """选择要替换的块（子类必须实现）"""
        pass
    
    def hit_rate(self):
        """计算命中率"""
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0
    
    def reset(self):
        """重置缓存状态"""
        self.blocks.clear()
        self.hits = 0
        self.misses = 0
        self.next_order = 0

class FIFO(CachePolicy):
    """先进先出策略"""
    def _select_to_replace(self):
        # 替换最早进入的块
        oldest = min(self.blocks, key=lambda b: b.order)
        return self.blocks.index(oldest)

class LRU(CachePolicy):
    """最近最少使用策略"""
    def _select_to_replace(self):
        # 替换最久未访问的块
        oldest = min(self.blocks, key=lambda b: b.last_time)
        return self.blocks.index(oldest)

class LFU(CachePolicy):
    """最少使用频率策略"""
    def _select_to_replace(self):
        # 先按访问次数，次数相同时按进入顺序
        oldest = min(self.blocks, key=lambda b: (b.count, b.order))
        return self.blocks.index(oldest)

class AdaptiveCache:
    """自适应缓存系统"""
    def __init__(self, capacity=4):
        self.policies = {
            'FIFO': FIFO(capacity),
            'LRU': LRU(capacity),
            'LFU': LFU(capacity)
        }
        self.selected = None
        self.selected_name = None
    
    def train(self, seq):
        """训练阶段：用前10次访问选择最佳策略"""
        print("=== 预测试阶段 (前10次) ===")
        best_name, best_rate = 'LRU', -1
        
        for name, policy in self.policies.items():
            policy.reset()
            for addr in seq:
                policy.access(addr)
            rate = policy.hit_rate()
            print(f"  {name}: 命中率={rate:.1%}")
            
            # 选择逻辑：命中率高优先，相同时LRU>LFU>FIFO
            priority = {'LRU': 3, 'LFU': 2, 'FIFO': 1}
            if rate > best_rate or (rate == best_rate and priority[name] > priority[best_name]):
                best_rate, best_name = rate, name
        
        self.selected = self.policies[best_name]
        self.selected_name = best_name
        self.selected.reset()
        print(f"→ 选定策略: {best_name} (命中率={best_rate:.1%})\n")
        return best_name
    
    def run(self, seq):
        """用选定策略运行完整序列"""
        print(f"=== 使用[{self.selected_name}]运行完整序列 ===")
        
        for i, addr in enumerate(seq, 1):
            hit, evicted = self.selected.access(addr)
            status = "命中" if hit else "未命中"
            cache_str = " ".join(str(b) for b in self.selected.blocks)
            replace_str = f"，替换{evicted}" if evicted else ""
            
            print(f"步骤{i:2d}: 访问{addr:2d} → {status:3s}，缓存: {cache_str:<20}{replace_str}")
        
        # 最终统计
        total = self.selected.hits + self.selected.misses
        rate = self.selected.hit_rate()
        print(f"\n{'='*40}")
        print(f"统计: 访问{total}次，命中{self.selected.hits}次，缺失{self.selected.misses}次")
        print(f"命中率: {rate:.1%}")
        print(f"{'='*40}")

# 测试
if __name__ == "__main__":
    # 测试数据
    seq1 = [1, 2, 3, 2, 4, 1]
    seq2 = [1, 3, 5, 3, 1, 2, 4, 5, 2, 1, 3, 4]
    seq3 = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2]
    
    for i, seq in enumerate([seq1, seq2, seq3], 1):
        print(f"\n{'#'*50}")
        print(f"测试序列{i}: {seq}")
        print(f"{'#'*50}")
        
        adaptive = AdaptiveCache(4)
        # 用前10个（或更少）进行训练
        train_len = min(10, len(seq))
        adaptive.train(seq[:train_len])
        # 运行完整序列
        adaptive.run(seq)
