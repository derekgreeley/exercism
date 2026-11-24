
<#
.DESCRIPTION
    A helper class acting as a data structure for saddle points.
#>
Class SaddlePoint {
    [int]$Row
    [int]$Column

    SaddlePoint($row, $col) {
        $this.Row = $row
        $this.Column = $col
    }

    [bool] Equals($other) {
        return $this.Row -eq $other.Row -and $this.Column -eq $other.Column
    }
}

Function Get-SaddlePoints {
    [CmdletBinding()]
    Param(
        [AllowEmptyCollection()]
        [int[][]]$Matrix
    )

    # Handle an empty matrix
    if ($Matrix.Count -eq 0) {
        return @()
    }

    $rowCount = $Matrix.Count
    $colCount = $Matrix[0].Count

    # Validate that the matrix is rectangular
    foreach ($row in $Matrix) {
        if ($row.Count -ne $colCount) {
            throw "Irregular matrix"
        }
    }

    if ($colCount -eq 0) {
        return @()
    }

    # Create arrays for row maximums and column minimums
    $rowMax = [int[]]::new($rowCount)
    $colMin = [int[]]::new($colCount)

    # Initialize row maximums
    for ($r = 0; $r -lt $rowCount; $r++) {
        $rowMax[$r] = [int]::MinValue
    }

    # Initialize column minimums
    for ($c = 0; $c -lt $colCount; $c++) {
        $colMin[$c] = [int]::MaxValue
    }

    # Calculate row maximums and column minimums
    for ($r = 0; $r -lt $rowCount; $r++) {
        for ($c = 0; $c -lt $colCount; $c++) {

            $value = $Matrix[$r][$c]

            if ($value -gt $rowMax[$r]) {
                $rowMax[$r] = $value
            }

            if ($value -lt $colMin[$c]) {
                $colMin[$c] = $value
            }
        }
    }

    # Identify all saddle points
    $result = [System.Collections.Generic.List[SaddlePoint]]::new()

    for ($r = 0; $r -lt $rowCount; $r++) {
        for ($c = 0; $c -lt $colCount; $c++) {

            $value = $Matrix[$r][$c]

            if ($value -eq $rowMax[$r] -and
                $value -eq $colMin[$c]) {

                $result.Add(
                    [SaddlePoint]::new(($r + 1), ($c + 1))
                )
            }
        }
    }

    return $result.ToArray()
}
