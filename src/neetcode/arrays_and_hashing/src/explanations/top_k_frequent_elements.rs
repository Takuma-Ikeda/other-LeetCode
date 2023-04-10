struct Solution;

use std::cmp::Ordering;
use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();

        for n in nums {
            *map.entry(n).or_default() += 1;
        }

        // 要素は (i32, i32) というタプルで管理
        let mut freq: Vec<(i32, i32)> = map.into_iter().collect();

        let res = if k == freq.len() as i32 {
            &freq
        } else {
            quick_select(&mut freq, k)
        };

        res.iter().map(|&(n, _)| n).collect()
    }
}

// k 番目に大きい要素を探すアルゴリズム "クイックソート" を実装: 平均的な実行時間は O(n) 最悪の場合の実行時間は O(n^2)
pub fn quick_select(slice: &mut [(i32, i32)], k: i32) -> &[(i32, i32)] {
    // 一気に複数の変数宣言、初期化を行う書き方
    let (mut pivot, mut i, mut j) = (0, 1, 1);

    // 0 番目の pivot と 1 番目の要素で比較していくので、スライスの開始は 1 で OK
    for index in 1..slice.len() {
        // タプルの (i32, i32) は (key, value) なので、value 同士比較するために .1 で指定
        if slice[index].1 >= slice[pivot].1 {
            // 現在の要素と j 番目の要素をスワップ
            slice.swap(index, j);
            j += 1;
        } else {
            // 現在の要素と i 番目の要素をスワップ
            slice.swap(index, i);
            i += 1;
            j += 1;
        }
    }

    // ピボット要素を正しい位置に移動
    slice.swap(pivot, i - 1);
    pivot = i - 1;

    // スライス内でピボットより大きい要素の数を計算
    let larger_items = (j - pivot) as i32;

    // larger_items と k を比較して 3 つのケースで処理
    match larger_items.cmp(&k) {
        // larger_items が k より小さい場合、スライスの左側を再帰的に処理
        Ordering::Less => quick_select(&mut slice[0..j], k),
        // larger_items が k より大きい場合、スライスの右側を再帰的に処理
        Ordering::Greater => quick_select(&mut slice[pivot + 1..j], k),
        // larger_items が k と等しい場合、ピボット位置から右側のスライスを返す
        Ordering::Equal => &slice[pivot..j],
    }
}

struct Case {
    expected: Vec<i32>,
    nums: Vec<i32>,
    k: i32,
}

struct TestCase {
    data: Vec<Case>,
}

impl TestCase {
    fn new() -> Self {
        TestCase {
            data: vec![
                Case {
                    expected: vec![1, 2],
                    nums: vec![1, 1, 1, 2, 2, 3],
                    k: 2,
                },
                Case {
                    expected: vec![1],
                    nums: vec![1],
                    k: 1,
                },
            ],
        }
    }
}

pub fn run() {
    execute();
}

#[test]
fn test() {
    execute();
}

fn execute() {
    let test_cases = TestCase::new();
    for case in test_cases.data.into_iter() {
        // 要素は順不同なので HashSet にして比較する
        let set1: HashSet<_> = Solution::top_k_frequent(case.nums, case.k)
            .into_iter()
            .collect();
        let set2: HashSet<_> = case.expected.into_iter().collect();
        assert_eq!(set1, set2);
    }
}
