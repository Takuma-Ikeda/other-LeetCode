struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();
        let mut result: Vec<i32> = vec![];

        for &num in nums.iter() {
            *map.entry(num).or_default() += 1;
        }

        let mut vec: Vec<(i32, i32)> = map.into_iter().collect();
        vec.sort_unstable_by(|a, b| b.1.cmp(&a.1));

        let start: usize = 0;
        let end: usize = k as usize;

        for (key, _value) in &vec[start..end] {
            result.push(*key);
        }

        result
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
