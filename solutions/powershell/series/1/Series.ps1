function Get-Slices {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [AllowEmptyString()]      # important: allow "" to bind, so we can throw our own error
        [string]$Series,

        [Parameter(Mandatory)]
        [int]$SliceLength
    )

    # ---- Validation ----
    if ($Series.Length -eq 0) {
        throw "Series cannot be empty."
    }

    if ($SliceLength -lt 0) {
        throw "Slice length cannot be negative."
    }

    if ($SliceLength -eq 0) {
        throw "Slice length cannot be zero."
    }

    if ($SliceLength -gt $Series.Length) {
        throw "Slice length cannot be greater than series length."
    }

    # ---- Build slices ----
    $result = @()
    $limit = $Series.Length - $SliceLength

    for ($i = 0; $i -le $limit; $i++) {
        $result += $Series.Substring($i, $SliceLength)
    }

    return $result
}
