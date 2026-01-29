function Test-Isbn {
    param(
        [AllowEmptyString()]
        [string]$Isbn
    )

    # Only hyphens are allowed as separators; remove them.
    $s = $Isbn -replace '-', ''

    # Must be exactly 10 chars after removing hyphens
    if ($s.Length -ne 10) {
        return $false
    }

    # First 9 must be digits
    if ($s.Substring(0, 9) -notmatch '^\d{9}$') {
        return $false
    }

    # Last must be a digit or X
    $last = $s[9]
    if ($last -notmatch '^[0-9X]$') {
        return $false
    }

    $sum = 0
    for ($i = 0; $i -lt 10; $i++) {
        $char = $s[$i]
        $value =
            if ($i -eq 9 -and $char -eq 'X') { 10 }
            else { [int]([string]$char) }   # safe here because validated digits

        $weight = 10 - $i
        $sum += $value * $weight
    }

    return (($sum % 11) -eq 0)
}
