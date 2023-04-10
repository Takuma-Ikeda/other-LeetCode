struct Solution;

use std::collections::HashSet;

impl Solution {
    // 遅くて LeetCode ではタイムアップしてしまう
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        use std::collections::HashMap;

        let mut result: Vec<Vec<String>> = Vec::new();
        let mut patterns: Vec<HashMap<char, i64>> = Vec::new();

        for str in strs.into_iter() {
            let mut is_new_pattern = true;

            // iter_mut で可変参照として取り出す
            // iter_mut はオリジナルの値に影響を与えるので clone してから使う
            for (i, pattern) in patterns.clone().iter_mut().enumerate() {
                for char in str.chars() {
                    *pattern.entry(char).or_default() -= 1;
                }

                // 可変参照なので into_values ではなく values を使う
                if pattern.values().all(|cnt| cnt == &0) {
                    result[i].push(str.clone());
                    is_new_pattern = false;
                    break;
                }
            }

            if !is_new_pattern {
                continue;
            }

            // 新しいパターンの場合
            let mut pattern: HashMap<char, i64> = HashMap::new();
            for char in str.chars() {
                *pattern.entry(char).or_default() += 1;
            }
            patterns.push(pattern);
            result.push(vec![str.clone()]);
        }

        for p in patterns.iter() {
            println!("{:?}", p);
        }

        result
    }
}

struct Case {
    expected: Vec<Vec<String>>,
    strs: Vec<String>,
}

struct TestCase {
    data: Vec<Case>,
}

impl TestCase {
    fn new() -> Self {
        TestCase {
            data: vec![
                Case {
                    expected: vec![
                        vec![
                            String::from("eat"),
                            String::from("tea"),
                            String::from("ate"),
                        ],
                        vec![String::from("tan"), String::from("nat")],
                        vec![String::from("bat")],
                    ],
                    strs: vec!["eat", "tea", "tan", "ate", "nat", "bat"]
                        .iter()
                        .map(|s| s.to_string())
                        .collect(),
                },
                Case {
                    expected: vec![vec![String::from("")]],
                    strs: vec![String::from("")],
                },
                Case {
                    expected: vec![vec![String::from("a")]],
                    strs: vec![String::from("a")],
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
        let set1: HashSet<_> = Solution::group_anagrams(case.strs).into_iter().collect();
        let set2: HashSet<_> = case.expected.into_iter().collect();
        assert_eq!(set1, set2);
    }
}
