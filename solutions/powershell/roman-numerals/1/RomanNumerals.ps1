
function Get-RomanNumerals {
    param(
        [int]$Number
    )

    # Validate the input range
    if ($Number -lt 1 -or $Number -gt 3999) {
        throw "Number has to be positive integer in range of 1-3999."
    }

    # Roman numeral values in descending order
    $values = @(
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    )

    $symbols = @(
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    )

    $result = ""

    # Convert using the largest possible value first
    for ($i = 0; $i -lt $values.Count; $i++) {

        while ($Number -ge $values[$i]) {
            $result += $symbols[$i]
            $Number -= $values[$i]
        }
    }

    return $result
}
