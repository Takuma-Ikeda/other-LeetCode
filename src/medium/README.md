# Problems

## Medium

1.  - [x] https://leetcode.com/problems/subrectangle-queries/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/subrectangle_queries.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_subrectangle_queries.py
    - deepcopy: 元のオブジェクト中に見つかった「オブジェクトのコピー」を挿入 ※ 通常の copy だと「参照」を挿入する
1.  - [x] https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/partitioning_into_minimum_number_of_deci_binary_numbers.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_partitioning_into_minimum_number_of_deci_binary_numbers.py
    - `max('123456789')` では 9 が返ってくる
1.  - [x] https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/minimum_number_of_operations_to_move_all_balls_to_each_box.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_minimum_number_of_operations_to_move_all_balls_to_each_box.py
    - ハッシュマップ
1.  - [x] https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/queries_on_number_of_points_inside_a_circle.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_queries_on_number_of_points_inside_a_circle.py
    - complex / sqrt: 正直よくわかってないのでリトライする
1.  - [x] https://leetcode.com/problems/deepest-leaves-sum/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/deepest_leaves_sum.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_deepest_leaves_sum.py
    - deque
1.  - [x] https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/group_the_people_given_the_group_size_they_belong_to.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_group_the_people_given_the_group_size_they_belong_to.py
    - ハッシュマップ / pop / `for idx in range(0, len(lst), key): answer.append(lst[idx:idx + key])` range のスキップ機能を使ったスライス
1.  - [x] https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/find_a_corresponding_node_of_a_binary_tree_in_a_clone_of_that_tree.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_find_a_corresponding_node_of_a_binary_tree_in_a_clone_of_that_tree.py
    - Tree からある一つの Node を見つけだしたらすぐ処理を中断して参照を返したいとき: return しながら再帰処理する `return traverse(o.left, c.left) or traverse(o.right, c.right)`
1.  - [x] https://leetcode.com/problems/max-increase-to-keep-city-skyline/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/max_increase_to_keep_city_skyline.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_max_increase_to_keep_city_skyline.py
    - range の代わりに `for i, j in product(range(5), range(5))` をすることもできる / `*変数` すると外側の `[]` を取り除くことができる (アンパック)
1.  - [x] https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/sum_of_nodes_with_even_valued_grandparent.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_sum_of_nodes_with_even_valued_grandparent.py
    - stack (DFS/BFS) / 再帰関数に「階層」「親の情報」「祖父母の情報」を渡す
1.  - [x] https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/widest_vertical_area_between_two_points_containing_no_points.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_widest_vertical_area_between_two_points_containing_no_points.py
    - ソート結果を list で保存する `arr = sorted(x for x, y in points)`
1.  - [x] https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/binary_search_tree_to_greater_sum_tree.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_binary_search_tree_to_greater_sum_tree.py
    - ノードの val を足し算していく。関数内関数の引数に演算結果を渡していく、もしくは、メンバ変数に演算結果を保持していく
1.  - [x] https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/maximum_twin_sum_of_a_linked_list.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_maximum_twin_sum_of_a_linked_list.py
    - ランナーテクニック
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
1.  - [] xxx
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/answer/xxx.py
    - https://github.com/Takuma-Ikeda/other-LeetCode/blob/master/src/medium/test_xxx.py
    - xxx
