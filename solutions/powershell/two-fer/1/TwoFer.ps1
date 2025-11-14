function Get-TwoFer {
    [CmdletBinding()]
    param(
        [Parameter(Position=0)]
        [string]$Name
    )

    process {
        if ([string]::IsNullOrWhiteSpace($Name)) {
            return "One for you, one for me"
        }
        return "One for $Name, one for me"
    }
}
