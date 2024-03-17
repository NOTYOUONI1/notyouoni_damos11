,[                       Read first binary number
  >                      Move to next cell
  ,[                     Read second binary number
    [-<+>]                Add it to the first number
    <-                    Move back to the first cell
    [->+<]                Move the sum to the second cell
    >[-<+>]               Add it to the first number again (carry)
    <-                    Move back to the second cell
    [->+<]                Move the carry to the third cell
    >[-<+>]               Add it to the second number
    <-                    Move back to the third cell
  ]
  <<<<[->+<]             Move the result to the first cell
  .                       Output the result
]

