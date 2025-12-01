function Invoke-RotationalCipher {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Text,

        [Parameter(Mandatory)]
        [int]$Shift
    )

    # Normalize shift to 0–25
    $shift = $Shift % 26

    $result = ""

    foreach ($char in $Text.ToCharArray()) {

        # Lowercase letters
        if ($char -ge 'a' -and $char -le 'z') {
            $base = [int][char]'a'
            $rotated = [char]((([int][char]$char - $base + $shift) % 26) + $base)
            $result += $rotated
            continue
        }

        # Uppercase letters
        if ($char -ge 'A' -and $char -le 'Z') {
            $base = [int][char]'A'
            $rotated = [char]((([int][char]$char - $base + $shift) % 26) + $base)
            $result += $rotated
            continue
        }

        # Non-letters: leave unchanged
        $result += $char
    }

    return $result
}
