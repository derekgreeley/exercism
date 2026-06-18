function Get-ScrabbleScore {
    [CmdletBinding()]
    param(
        [string]$Word,
        [switch]$Bonus
    )

    # Empty or whitespace word => score 0
    if ($null -eq $Word -or $Word.Length -eq 0) {
        return 0
    }

    # Letter-to-score map
    $scoreMap = @{
        'a' = 1; 'e' = 1; 'i' = 1; 'o' = 1; 'u' = 1; 'l' = 1; 'n' = 1; 'r' = 1; 's' = 1; 't' = 1
        'd' = 2; 'g' = 2
        'b' = 3; 'c' = 3; 'm' = 3; 'p' = 3
        'f' = 4; 'h' = 4; 'v' = 4; 'w' = 4; 'y' = 4
        'k' = 5
        'j' = 8; 'x' = 8
        'q' = 10; 'z' = 10
    }

    $total = 0

    # Normalize to lowercase and iterate characters
    foreach ($ch in $Word.ToLowerInvariant().ToCharArray()) {
        $key = [string]$ch   # convert [char] → [string] so it matches hashtable keys

        if ($scoreMap.ContainsKey($key)) {
            $total += $scoreMap[$key]
        }
    }

    if ($Bonus) {
        $total *= 2
    }

    return $total
}
