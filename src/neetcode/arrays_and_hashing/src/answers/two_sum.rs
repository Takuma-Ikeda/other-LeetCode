struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        if nums.len() == 2 {
            return vec![0, 1];
        }

        let mut result: Vec<i32> = Vec::new();

        for (index1, &value1) in nums.iter().enumerate() {
            let t = &target;
            let diff = t - value1;

            if diff <= 0 {
                continue;
            }

            if let Some(index2) = nums.iter().position(|&x| x == diff) {
                if index1 == index2 {
                    continue;
                }
                result.push(index1 as i32);
                result.push(index2 as i32);
                break
            }
        }
        result
    }
}

struct Case {
    expected: Vec<i32>,
    nums: Vec<i32>,
    target: i32,
}

struct TestCase {
    data: Vec<Case>,
}

impl TestCase {
    fn new() -> Self {
        TestCase {
            data: vec![
                Case {
                    expected: vec![0, 1],
                    nums: vec![2,7,11,15],
                    target: 9,
                },
                Case {
                    expected: vec![1, 2],
                    nums: vec![3,2,4],
                    target: 6,
                },
                Case {
                    expected: vec![0, 1],
                    nums: vec![3,3],
                    target: 6,
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
        assert_eq!(case.expected, Solution::two_sum(case.nums, case.target));
    }
}
