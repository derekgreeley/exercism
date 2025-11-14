function Invoke-BinarySearch {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [AllowEmptyCollection()]
        [int[]]$Array,

        [Parameter(Mandatory, Position=1)]
        [int]$Value
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        # Standard iterative binary search on a sorted array
        $left  = 0
        $right = $Array.Length - 1

        while ($left -le $right) {
            # Avoid overflow, though with ints here it's fine; still doing safe mid
            $mid = $left + [int](($right - $left) / 2)

            if ($Array[$mid] -eq $Value) {
                return $mid
            }
            elseif ($Array[$mid] -lt $Value) {
                $left = $mid + 1
            }
            else {
                $right = $mid - 1
            }
        }

        throw "error: value not in array"
    }
}
