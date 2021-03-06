using System.Collections.Generic;
using System.Linq;

namespace Exercism.CSharp.Solutions.MatchingBracketsExercise
{
    public static class MatchingBrackets
    {
        private static readonly IReadOnlyDictionary<char, char> wrapperPairs = new Dictionary<char, char>
        {
            ['('] = ')',
            ['['] = ']',
            ['{'] = '}'
        };

        public static bool IsPaired(string input)
        {
            var openGroups = new Stack<char>();

            foreach (var wrapper in input.Where(IsWrapper))
            {
                if (wrapperPairs.Keys.Contains(wrapper))
                {
                    // It is a opening wrapper, add to the stack.
                    openGroups.Push(wrapper);
                }
                else if (openGroups.Count > 0)
                {
                    // It is a closing wrapper with existing opening wrapper on the stack
                    // check if it is the correct pair
                    if (!openGroups.Peek().IsCorrectPair(wrapper))
                    {
                        return false;
                    }

                    // remove this opening wrapper from the stack
                    openGroups.Pop();
                }
                else
                {
                    // It is a closing wrapper without a opening wrapper.
                    return false;
                }
            }

            // All opening wrappers should have been matched.
            return openGroups.Count == 0;
        }

        private static bool IsWrapper(this char ch) =>
            wrapperPairs.Keys.Contains(ch) || wrapperPairs.Values.Contains(ch);

        private static bool IsCorrectPair(this char opening, char closing) =>
            wrapperPairs[opening] == closing;
    }
}