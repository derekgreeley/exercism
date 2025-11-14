function Get-ColorCodeValue {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [ValidateNotNullOrEmpty()]
        [string[]]$Colors
    )

    begin {
        # mapping of color -> digit
        $colorMap = @{
            black  = 0
            brown  = 1
            red    = 2
            orange = 3
            yellow = 4
            green  = 5
            blue   = 6
            violet = 7
            grey   = 8
            white  = 9
        }
    }

    process {
        try {
            # Take only the first two colors, ignore the rest
            $pair = $Colors | Select-Object -First 2

            if ($pair.Count -lt 2) {
                throw "At least two colors are required."
            }

            # Convert to digits
            $digits = $pair | ForEach-Object {
                if (-not $colorMap.ContainsKey($_.ToLower())) {
                    throw "Invalid color: $_"
                }
                $colorMap[$_.ToLower()]
            }

            # Combine into number string, then cast to int
            $numberString = ($digits -join '')
            return [int]$numberString
        }
        catch {
            throw
        }
    }
}
