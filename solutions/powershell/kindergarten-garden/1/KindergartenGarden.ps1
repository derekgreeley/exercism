
Class Garden {
    [string[]]$Rows
    [string[]]$Students

    # Constructor using the default student list
    Garden([string]$Diagram) {
        $this.Rows = $Diagram -split '\r?\n'

        $this.Students = @(
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
        )
    }

    # Constructor using a custom student list
    Garden([string]$Diagram, [string[]]$Students) {
        $this.Rows = $Diagram -split '\r?\n'
        $this.Students = @($Students | Sort-Object)
    }

    [string[]] GetPlants([string]$Student) {

        $studentIndex = [array]::IndexOf(
            $this.Students,
            $Student
        )

        if ($studentIndex -eq -1) {
            throw "Student not found: $Student"
        }

        # Each student receives two cups per row
        $start = $studentIndex * 2

        $plantMap = @{
            'G' = "Grass"
            'C' = "Clover"
            'R' = "Radishes"
            'V' = "Violets"
        }

        # Extract plants in row order
        $codes = @(
            $this.Rows[0][$start]
            $this.Rows[0][$start + 1]
            $this.Rows[1][$start]
            $this.Rows[1][$start + 1]
        )

        $plants = @()

        foreach ($code in $codes) {
            $plants += $plantMap[[string]$code]
        }

        return $plants
    }
}
