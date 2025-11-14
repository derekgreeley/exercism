function Invoke-ArmstrongNumbers {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [int]$Number
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        # Convert number to string to easily iterate digits
        $digits = $Number.ToString().ToCharArray()
        $power = $digits.Length

        $sum = 0
        foreach ($d in $digits) {
            $digitVal = [int]$d.ToString()
            $sum += [math]::Pow($digitVal, $power)
        }

        return ($sum -eq $Number)
    }
}
