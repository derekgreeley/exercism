function Invoke-Encode {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string]$Phrase
    )

    # Normalize: lowercase, keep only letters/digits
    $clean = ($Phrase.ToLowerInvariant() -replace '[^a-z0-9]', '')

    # Atbash transform
    $chars = $clean.ToCharArray()
    for ($i = 0; $i -lt $chars.Length; $i++) {
        $c = $chars[$i]
        if ($c -ge 'a' -and $c -le 'z') {
            $chars[$i] = [char]([int][char]'a' + ([int][char]'z' - [int][char]$c))
        }
        # digits stay as-is
    }
    $encoded = -join $chars

    # Group into chunks of 5
    if ($encoded.Length -eq 0) { return "" }

    $groups = New-Object System.Collections.Generic.List[string]
    for ($i = 0; $i -lt $encoded.Length; $i += 5) {
        $len = [math]::Min(5, $encoded.Length - $i)
        $groups.Add($encoded.Substring($i, $len))
    }
    return ($groups -join ' ')
}

function Invoke-Decode {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string]$Phrase
    )

    # Normalize: lowercase, remove spaces, keep only letters/digits
    $clean = ($Phrase.ToLowerInvariant() -replace '\s+', '') -replace '[^a-z0-9]', ''

    # Atbash transform (same as encode), but no regrouping
    $chars = $clean.ToCharArray()
    for ($i = 0; $i -lt $chars.Length; $i++) {
        $c = $chars[$i]
        if ($c -ge 'a' -and $c -le 'z') {
            $chars[$i] = [char]([int][char]'a' + ([int][char]'z' - [int][char]$c))
        }
    }
    return (-join $chars)
}
