function Get-ReverseString {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [AllowEmptyString()]
        [string]$Forward
    )

    process {
        # Fast path for empty strings
        if ($Forward.Length -eq 0) { return "" }

        # Reverse safely without pipelines or by-ref trickery
        $chars = $Forward.ToCharArray()
        [Array]::Reverse($chars)
        -join $chars
    }
}


