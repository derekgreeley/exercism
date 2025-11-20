function Invoke-Etl {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [hashtable]$Legacy
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        $result = @{}

        foreach ($entry in $Legacy.GetEnumerator()) {
            # Keys are scores (1,2,3,...)
            $score = [int]$entry.Key
            # Values are arrays of uppercase letters
            foreach ($letter in $entry.Value) {
                $key = $letter.ToLowerInvariant()
                $result[$key] = $score
            }
        }

        return $result
    }
}
