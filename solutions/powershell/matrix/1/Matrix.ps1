function Invoke-Row {
    param(
        [string]$String,
        [int]$Index
    )

    # Split into rows
    $rows = $String -split "`n"

    # Get the target row (1-based index)
    $row = $rows[$Index - 1]

    # Split by whitespace and convert to int
    $result = @()
    foreach ($value in ($row -split '\s+')) {
        if ($value -ne "") {
            $result += [int]$value
        }
    }

    return $result
}

function Invoke-Column {
    param(
        [string]$String,
        [int]$Index
    )

    $rows = $String -split "`n"
    $result = @()

    foreach ($row in $rows) {
        $values = @()

        foreach ($value in ($row -split '\s+')) {
            if ($value -ne "") {
                $values += [int]$value
            }
        }

        # Only add if column exists (handles jagged/non-square)
        if ($Index -le $values.Count) {
            $result += $values[$Index - 1]
        }
    }

    return $result
}