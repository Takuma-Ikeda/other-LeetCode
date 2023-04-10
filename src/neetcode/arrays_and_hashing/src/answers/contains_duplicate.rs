struct Solution;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        use std::collections::HashMap;

        let mut result = false;
        let mut hashmap = HashMap::new();

        for num in nums {
            if hashmap.get(&num).is_none() {
                hashmap.insert(num, num);
                continue;
            }
            result = true;
            break;
        }
        result
    }
}

struct Case {
    expected: bool,
    nums: Vec<i32>,
}

struct TestCase {
    data: Vec<Case>,
}

impl TestCase {
    fn new() -> Self {
        TestCase {
            data: vec![
                Case {
                    expected: true,
                    nums: vec![1, 2, 3, 1],
                },
                Case {
                    expected: false,
                    nums: vec![1, 2, 3, 4],
                },
                Case {
                    expected: true,
                    nums: vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
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
        assert_eq!(case.expected, Solution::contains_duplicate(case.nums));
    }
}
