class Roster {
    [System.Collections.Generic.List[object]] $Students

    Roster() {
        # Initialize the internal list of students
        $this.Students = [System.Collections.Generic.List[object]]::new()
    }

    [bool] AddStudent([int]$Grade, [string]$Name) {
        # Do not allow the same student name to appear more than once
        foreach ($s in $this.Students) {
            if ($s.Name -eq $Name) {
                # Already present in some grade -> reject
                return $false
            }
        }

        # Add new student as a PSCustomObject with Grade and Name
        $student = [pscustomobject]@{
            Grade = $Grade
            Name  = $Name
        }

        $this.Students.Add($student)
        return $true
    }

    # Get full roster, sorted by grade then by name
    [object[]] GetRoster() {
        if ($this.Students.Count -eq 0) {
            return @()
        }

        return $this.Students | Sort-Object Grade, Name
    }

    # Get roster for a specific grade, sorted by name
    [object[]] GetRoster([int]$Grade) {
        $filtered = $this.Students | Where-Object { $_.Grade -eq $Grade }

        if (-not $filtered) {
            return @()
        }

        return $filtered | Sort-Object Name
    }
}
