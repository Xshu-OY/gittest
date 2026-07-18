# """
# 智能缓存替换策略自适应系统
# 计算机系统I 课程设计

# 功能：
# 1. 实现固定大小为4块的缓存结构
# 2. 支持FIFO、LRU、LFU三种经典缓存替换算法
# 3. 自适应策略：前10次访问预测试，自动选择最优策略
# 4. 详细输出每一步过程与最终统计结果
# """

# from typing import List, Optional
# from dataclasses import dataclass, field
# from enum import Enum
# import time


# class ReplacementStrategy(Enum):
#     FIFO = "FIFO"
#     LRU = "LRU"
#     LFU = "LFU"
#     ADAPTIVE = "自适应"


# @dataclass
# class CacheBlock:
#     """缓存块数据结构"""
#     address: int
#     entry_order: int = 0          # 进入顺序（FIFO用）
#     last_access_time: float = 0.0  # 最后访问时间（LRU用）
#     access_count: int = 0          # 累计访问次数（LFU用）

#     def update_access(self):
#         """更新访问信息"""
#         self.last_access_time = time.time()
#         self.access_count += 1


# @dataclass
# class CacheStats:
#     """缓存统计信息"""
#     total_access: int = 0
#     hits: int = 0
#     misses: int = 0

#     @property
#     def hit_rate(self) -> float:
#         return self.hits / self.total_access * 100 if self.total_access > 0 else 0


# class Cache:
#     """缓存模拟器"""

#     CAPACITY = 4

#     def __init__(self, strategy: ReplacementStrategy = ReplacementStrategy.FIFO):
#         self.blocks: List[Optional[CacheBlock]] = [None] * self.CAPACITY
#         self.strategy = strategy
#         self.access_count = 0  # 全局访问计数器（用于FIFO排序）
#         self._init_time = time.time()

#     def find_block(self, address: int) -> tuple[bool, int]:
#         """查找地址是否在缓存中，返回(是否命中, 块索引)"""
#         for i, block in enumerate(self.blocks):
#             if block and block.address == address:
#                 return True, i
#         return False, -1

#     def get_empty_slot(self) -> int:
#         """获取空闲槽位索引，无空闲返回-1"""
#         for i, block in enumerate(self.blocks):
#             if block is None:
#                 return i
#         return -1

#     def select_victim_fifo(self) -> int:
#         """FIFO选择victim：选择进入最早的"""
#         min_order = float('inf')
#         victim_idx = 0
#         for i, block in enumerate(self.blocks):
#             if block and block.entry_order < min_order:
#                 min_order = block.entry_order
#                 victim_idx = i
#         return victim_idx

#     def select_victim_lru(self) -> int:
#         """LRU选择victim：选择最久未访问的"""
#         min_time = float('inf')
#         victim_idx = 0
#         for i, block in enumerate(self.blocks):
#             if block and block.last_access_time < min_time:
#                 min_time = block.last_access_time
#                 victim_idx = i
#         return victim_idx

#     def select_victim_lfu(self) -> int:
#         """LFU选择victim：选择访问次数最少的，相同按FIFO"""
#         min_count = float('inf')
#         min_order = float('inf')
#         victim_idx = 0
#         for i, block in enumerate(self.blocks):
#             if block:
#                 if block.access_count < min_count:
#                     min_count = block.access_count
#                     min_order = block.entry_order
#                     victim_idx = i
#                 elif block.access_count == min_count:
#                     if block.entry_order < min_order:
#                         min_order = block.entry_order
#                         victim_idx = i
#         return victim_idx

#     def select_victim(self) -> int:
#         """根据策略选择victim块"""
#         if self.strategy == ReplacementStrategy.FIFO:
#             return self.select_victim_fifo()
#         elif self.strategy == ReplacementStrategy.LRU:
#             return self.select_victim_lru()
#         elif self.strategy == ReplacementStrategy.LFU:
#             return self.select_victim_lfu()
#         return 0

#     def access(self, address: int) -> tuple[bool, str]:
#         """
#         访问指定地址，返回(是否命中, 操作描述)
#         """
#         hit, idx = self.find_block(address)

#         if hit:
#             self.blocks[idx].update_access()
#             return True, f"命中"
#         else:
#             empty_slot = self.get_empty_slot()

#             if empty_slot != -1:
#                 self.blocks[empty_slot] = CacheBlock(
#                     address=address,
#                     entry_order=self.access_count,
#                     last_access_time=time.time(),
#                     access_count=1
#                 )
#                 self.access_count += 1
#                 return False, f"未命中->写入空槽{empty_slot}"
#             else:
#                 victim_idx = self.select_victim()
#                 old_addr = self.blocks[victim_idx].address
#                 self.blocks[victim_idx] = CacheBlock(
#                     address=address,
#                     entry_order=self.access_count,
#                     last_access_time=time.time(),
#                     access_count=1
#                 )
#                 self.access_count += 1
#                 return False, f"未命中->替换块{victim_idx}({old_addr})"

#     def get_content(self) -> List[str]:
#         """获取缓存内容描述"""
#         return [f"[{b.address}]" if b else "[  ]" for b in self.blocks]


# class AdaptiveCacheSimulator:
#     """自适应缓存模拟器"""

#     TEST_SIZE = 10  # 前10次访问用于测试

#     def __init__(self, access_sequence: List[int]):
#         self.access_sequence = access_sequence
#         self.test_results = {}
#         self.selected_strategy = None
#         self.stats = CacheStats()
#         self.log = []

#     def test_strategy(self, strategy: ReplacementStrategy) -> tuple[float, int, int]:
#         """测试某策略在前TEST_SIZE次访问的命中率"""
#         cache = Cache(strategy)
#         hits = 0
#         misses = 0

#         for i in range(min(self.TEST_SIZE, len(self.access_sequence))):
#             address = self.access_sequence[i]
#             hit, _ = cache.access(address)
#             if hit:
#                 hits += 1
#             else:
#                 misses += 1

#         hit_rate = hits / (hits + misses) * 100 if (hits + misses) > 0 else 0
#         return hit_rate, hits, misses

#     def run_adaptive_test(self):
#         """运行自适应测试阶段"""
#         self.log.append("=" * 60)
#         self.log.append("【自适应策略预测试阶段】")
#         self.log.append(f"使用前{self.TEST_SIZE}次访问测试各策略...")
#         self.log.append("")

#         strategies = [
#             ReplacementStrategy.FIFO,
#             ReplacementStrategy.LRU,
#             ReplacementStrategy.LFU
#         ]

#         # 优先级顺序：LRU > LFU > FIFO（当命中率相同时）
#         priority = {
#             ReplacementStrategy.LRU: 3,
#             ReplacementStrategy.LFU: 2,
#             ReplacementStrategy.FIFO: 1
#         }

#         for strategy in strategies:
#             hit_rate, hits, misses = self.test_strategy(strategy)
#             self.test_results[strategy] = {
#                 'hit_rate': hit_rate,
#                 'hits': hits,
#                 'misses': misses
#             }
#             self.log.append(f"{strategy.value:6s} | 命中: {hits:2d} | 未命中: {misses:2d} | 命中率: {hit_rate:5.1f}%")

#         # 选择最佳策略
#         best_strategy = max(
#             strategies,
#             key=lambda s: (self.test_results[s]['hit_rate'], priority[s])
#         )
#         self.selected_strategy = best_strategy

#         self.log.append("")
#         self.log.append(f"选择最优策略: {best_strategy.value} (命中率: {self.test_results[best_strategy]['hit_rate']:.1f}%)")
#         self.log.append("=" * 60)
#         self.log.append("")

#     def run_full_simulation(self):
#         """运行完整模拟"""
#         if self.selected_strategy is None:
#             self.run_adaptive_test()

#         cache = Cache(self.selected_strategy)

#         self.log.append("【完整访问序列执行】")
#         self.log.append("-" * 60)
#         self.log.append(f"{'步骤':^4} | {'访问':^4} | {'结果':^12} | {'缓存状态':^20} | {'策略':^8}")
#         self.log.append("-" * 60)

#         step = 1
#         for address in self.access_sequence:
#             hit, action = cache.access(address)

#             if hit:
#                 self.stats.hits += 1
#             else:
#                 self.stats.misses += 1
#             self.stats.total_access += 1

#             content = " ".join(cache.get_content())
#             self.log.append(f"{step:^4} | {address:^4} | {action:^12} | {content:^20} | {self.selected_strategy.value:^8}")
#             step += 1

#         self.log.append("-" * 60)

#     def print_results(self):
#         """打印完整结果"""
#         for line in self.log:
#             print(line)

#         print("")
#         print("=" * 60)
#         print("【最终统计结果】")
#         print("=" * 60)
#         print(f"总访问次数: {self.stats.total_access}")
#         print(f"总命中次数: {self.stats.hits}")
#         print(f"总缺失次数: {self.stats.misses}")
#         print(f"整体命中率: {self.stats.hit_rate:.2f}%")
#         print("=" * 60)


# def run_single_strategy_test(access_sequence: List[int], strategy: ReplacementStrategy):
#     """单独测试某种策略（用于对比分析）"""
#     cache = Cache(strategy)
#     stats = CacheStats()

#     log = []
#     log.append(f"\n{'=' * 60}")
#     log.append(f"{strategy.value} 策略测试")
#     log.append(f"{'=' * 60}")
#     log.append(f"{'步骤':^4} | {'访问':^4} | {'结果':^12} | {'缓存状态':^20}")
#     log.append("-" * 60)

#     for i, address in enumerate(access_sequence):
#         hit, action = cache.access(address)

#         if hit:
#             stats.hits += 1
#         else:
#             stats.misses += 1
#         stats.total_access += 1

#         content = " ".join(cache.get_content())
#         log.append(f"{i+1:^4} | {address:^4} | {action:^12} | {content:^20}")

#     for line in log:
#         print(line)

#     print("-" * 60)
#     print(f"总访问: {stats.total_access} | 命中: {stats.hits} | 未命中: {stats.misses} | 命中率: {stats.hit_rate:.2f}%")


# def demo():
#     """演示三组测试数据"""

#     # 测试数据1：经典示例
#     test_data_1 = [1, 2, 3, 2, 4, 1]

#     # 测试数据2：较多重复访问
#     test_data_2 = [1, 2, 1, 3, 1, 4, 2, 1, 3, 2, 4, 1]

#     # 测试数据3：较长序列
#     test_data_3 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 5, 1, 3, 2, 4, 1]

#     datasets = [
#         ("测试数据1（经典示例）", test_data_1),
#         ("测试数据2（重复访问）", test_data_2),
#         ("测试数据3（较长序列）", test_data_3)
#     ]

#     print("=" * 70)
#     print(" " * 20 + "智能缓存替换策略自适应系统")
#     print(" " * 25 + "计算机系统I 课程设计")
#     print("=" * 70)

#     for name, data in datasets:
#         print(f"\n\n{'#' * 70}")
#         print(f"## {name}")
#         print(f"## 访问序列: {data}")
#         print(f"{'#' * 70}")

#         # 运行自适应策略
#         simulator = AdaptiveCacheSimulator(data)
#         simulator.run_full_simulation()
#         simulator.print_results()

#     # 额外对比：三种策略分别运行同一数据集
#     print("\n\n" + "=" * 70)
#     print(" " * 25 + "策略对比分析")
#     print("=" * 70)
#     print(f"访问序列: {test_data_2}")
#     print("")

#     for strategy in [ReplacementStrategy.FIFO, ReplacementStrategy.LRU, ReplacementStrategy.LFU]:
#         run_single_strategy_test(test_data_2, strategy)


# if __name__ == "__main__":
#     demo()







# """
# 自适应缓存替换策略模拟器
# 设计目标：基于指定文档，实现FIFO, LRU, LFU及自适应策略，缓存大小为4。
# """

# import time
# from abc import ABC, abstractmethod

# class CacheBlock:
#     """
#     缓存块类
#     对应文档要求：每块必须记录【地址、进入顺序、最后访问时间、累计访问次数】
#     """
#     def __init__(self, address, entry_order):
#         self.address = address          # 存储的地址
#         self.entry_order = entry_order  # 进入缓存的顺序（用于FIFO）
#         self.last_access_time = time.time()  # 最后访问时间戳（用于LRU）
#         self.access_count = 1           # 累计访问次数（用于LFU）, 创建时即第一次访问

#     def update_on_hit(self):
#         """命中时的更新操作"""
#         self.last_access_time = time.time()
#         self.access_count += 1

#     def __str__(self):
#         return f"[Addr:{self.address}, Order:{self.entry_order}]"

# class CacheReplacementPolicy(ABC):
#     """
#     缓存替换策略抽象基类
#     定义所有策略必须实现的核心接口。
#     """
#     def __init__(self, capacity=4):
#         self.capacity = capacity
#         self.cache = []  # 用列表模拟缓存，列表元素为CacheBlock对象
#         self.hit_count = 0
#         self.miss_count = 0
#         self.current_order = 0  # 全局顺序计数器，用于标记块进入缓存的先后

#     def access(self, address):
#         """
#         处理一次地址访问。
#         返回：(is_hit, evicted_address)
#         """
#         # 1. 检查是否命中
#         for block in self.cache:
#             if block.address == address:
#                 # 文档要求：命中时更新最后访问时间，访问次数+1
#                 block.update_on_hit()
#                 self.hit_count += 1
#                 return True, None  # 命中，无需替换

#         # 2. 未命中
#         self.miss_count += 1
#         evicted_address = None

#         if len(self.cache) < self.capacity:
#             # 缓存未满：直接加入
#             self.current_order += 1
#             new_block = CacheBlock(address, self.current_order)
#             self.cache.append(new_block)
#         else:
#             # 缓存已满：调用策略决定替换哪个块
#             index_to_replace = self._select_block_to_replace()
#             evicted_block = self.cache.pop(index_to_replace)
#             evicted_address = evicted_block.address
#             # 加入新块
#             self.current_order += 1
#             new_block = CacheBlock(address, self.current_order)
#             self.cache.append(new_block)

#         return False, evicted_address

#     @abstractmethod
#     def _select_block_to_replace(self):
#         """
#         选择要替换的缓存块索引（子类必须实现）。
#         对应文档要求：FIFO、LRU、LFU各自的核心规则。
#         """
#         pass

#     def get_hit_rate(self):
#         """计算命中率"""
#         total = self.hit_count + self.miss_count
#         return self.hit_count / total if total > 0 else 0.0

#     def reset_stats(self):
#         """重置统计信息（用于自适应策略的预测试阶段）"""
#         self.cache.clear()
#         self.hit_count = 0
#         self.miss_count = 0
#         self.current_order = 0

# # ========== 三种具体策略的实现 ==========
# class FIFO(CacheReplacementPolicy):
#     """先进先出策略：替换最早进入（entry_order最小）的块。"""
#     def _select_block_to_replace(self):
#         # 在缓存中寻找进入顺序最小的块
#         min_order = min(block.entry_order for block in self.cache)
#         for i, block in enumerate(self.cache):
#             if block.entry_order == min_order:
#                 return i

# class LRU(CacheReplacementPolicy):
#     """最近最少使用策略：替换最久未被访问（last_access_time最小）的块。"""
#     def _select_block_to_replace(self):
#         # 在缓存中寻找访问时间最早的块
#         oldest_time = min(block.last_access_time for block in self.cache)
#         for i, block in enumerate(self.cache):
#             if block.last_access_time == oldest_time:
#                 return i

# class LFU(CacheReplacementPolicy):
#     """最少使用频率策略：替换访问次数最少的块；次数相同时，按 FIFO规则替换。"""
#     def _select_block_to_replace(self):
#         # 1. 找到最小的访问次数
#         min_count = min(block.access_count for block in self.cache)
#         # 2. 在所有具有最小访问次数的块中，找到最早进入的（entry_order最小）
#         candidate_blocks = [block for block in self.cache if block.access_count == min_count]
#         oldest_block = min(candidate_blocks, key=lambda b: b.entry_order)
#         # 3. 返回这个块在缓存中的索引
#         for i, block in enumerate(self.cache):
#             if block is oldest_block:
#                 return i

# # ========== 自适应策略核心类 ==========
# class AdaptiveCache:
#     """
#     自适应缓存系统
#     对应文档要求：
#     1. 截取前10次访问作为测试样本。
#     2. 分别用FIFO、LRU、LFU独立测试前10次访问，计算命中率。
#     3. 选择命中率最高的策略；命中率相同时，按LRU>LFU>FIFO优先级选择。
#     4. 用选定策略跑完整个访问序列。
#     """
#     def __init__(self, capacity=4):
#         self.capacity = capacity
#         self.policies = {
#             'FIFO': FIFO(capacity),
#             'LRU': LRU(capacity),
#             'LFU': LFU(capacity)
#         }
#         self.selected_policy_name = None
#         self.selected_policy = None
#         self.final_hit_rate = 0.0

#     def train_and_select_policy(self, training_sequence):
#         """
#         训练阶段：使用前10次访问测试并选择最佳策略。
#         """
#         print("=== 自适应策略预测试阶段 (前10次访问) ===")
#         best_policy_name = 'LRU'  # 默认按优先级LRU最高
#         best_hit_rate = -1

#         for policy_name, policy in self.policies.items():
#             policy.reset_stats()  # 确保每个策略从干净状态开始测试
#             for addr in training_sequence:
#                 policy.access(addr)
#             hit_rate = policy.get_hit_rate()
#             print(f"  策略 {policy_name}: 命中次数={policy.hit_count}, 命中率={hit_rate:.2%}")

#             # 选择逻辑：命中率更高者胜出；相同时，由于字典遍历顺序是FIFO->LRU->LFU，
#             # 我们需要手动实现 LRU > LFU > FIFO 的优先级
#             if (hit_rate > best_hit_rate) or \
#                (abs(hit_rate - best_hit_rate) < 1e-9 and self._get_priority(policy_name) > self._get_priority(best_policy_name)):
#                 best_hit_rate = hit_rate
#                 best_policy_name = policy_name

#         self.selected_policy_name = best_policy_name
#         self.selected_policy = self.policies[best_policy_name]
#         self.selected_policy.reset_stats()  # 清空测试数据，准备正式运行
#         print(f"-> 选定策略: {self.selected_policy_name} (测试命中率: {best_hit_rate:.2%})\n")
#         return best_policy_name

#     def _get_priority(self, policy_name):
#         """为策略分配优先级，用于处理命中率相同的情况。LRU(3) > LFU(2) > FIFO(1)"""
#         priority_map = {'LRU': 3, 'LFU': 2, 'FIFO': 1}
#         return priority_map.get(policy_name, 0)

#     def run_full_sequence(self, full_sequence):
#         """
#         运行阶段：使用选定的策略处理整个访问序列，并输出详细步骤和统计。
#         """
#         print(f"=== 使用策略 [{self.selected_policy_name}] 运行完整序列 ===")
#         step = 0
#         for addr in full_sequence:
#             step += 1
#             is_hit, evicted_addr = self.selected_policy.access(addr)
#             hit_miss_str = "命中" if is_hit else "未命中"
#             evicted_str = f"，替换了地址 {evicted_addr}" if evicted_addr is not None else ""

#             # 格式化当前缓存内容
#             cache_content = " ".join([str(block) for block in self.selected_policy.cache])

#             # 输出每一步结果，格式对齐
#             print(f"步骤{step:2d}: 访问地址 {addr:2d} -> {hit_miss_str:3s}， 缓存内容: {cache_content:<40} {evicted_str}")

#         # 最终统计
#         total = self.selected_policy.hit_count + self.selected_policy.miss_count
#         self.final_hit_rate = self.selected_policy.get_hit_rate()
#         print("\n" + "="*50)
#         print("最终统计:")
#         print(f"  总访问次数: {total}")
#         print(f"  总命中次数: {self.selected_policy.hit_count}")
#         print(f"  总缺失次数: {self.selected_policy.miss_count}")
#         print(f"  整体命中率: {self.final_hit_rate:.2%}")
#         print("="*50)

# # ========== 主程序：测试与演示 ==========
# def main():
#     """
#     主函数，组织整个实验流程。
#     对应文档要求：对3组测试数据完整测试。
#     """
#     # 文档中的示例访问序列（第1组）
#     test_sequence_1 = [1, 2, 3, 2, 4, 1]
#     # 另外补充两组测试序列
#     test_sequence_2 = [1, 3, 5, 3, 1, 2, 4, 5, 2, 1, 3, 4]
#     test_sequence_3 = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2]

#     all_sequences = [("测试序列1", test_sequence_1),
#                      ("测试序列2", test_sequence_2),
#                      ("测试序列3", test_sequence_3)]

#     for seq_name, full_seq in all_sequences:
#         print(f"\n{'#'*60}")
#         print(f"开始处理 {seq_name}: {full_seq}")
#         print(f"{'#'*60}")

#         # 1. 确保访问序列长度 >= 10，否则以实际长度作为训练长度
#         training_length = min(10, len(full_seq))
#         training_seq = full_seq[:training_length]
#         remaining_seq = full_seq[training_length:]

#         # 2. 创建自适应缓存并训练
#         adaptive_cache = AdaptiveCache(capacity=4)
#         adaptive_cache.train_and_select_policy(training_seq)

#         # 3. 用选定的策略运行完整序列
#         # 注意：训练阶段的前10次访问结果不计入最终统计，因为 selected_policy 已被 reset_stats。
#         # 我们需要从第一步开始，重新用选定的策略处理“整个”序列。
#         adaptive_cache.selected_policy.reset_stats()  # 再次重置，准备从头运行
#         adaptive_cache.run_full_sequence(full_seq)  # 这次运行的是完整的原始序列

# if __name__ == "__main__":
#     main()





import time
from abc import ABC, abstractmethod

class CacheBlock:
    """缓存块，包含地址、顺序、最后访问时间和访问次数"""
    def __init__(self, address, order):
        self.addr = address
        self.order = order
        self.last_time = time.time()
        self.count = 1
    
    def hit_update(self):
        """命中时更新时间和次数"""
        self.last_time = time.time()
        self.count += 1
    
    def __str__(self):
        return f"[{self.addr}]"

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














