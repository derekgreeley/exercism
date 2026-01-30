# RobotName.ps1

class Robot {
    [string] $Name

    hidden static [string[]] $Pool = @()
    hidden static [int] $Index = 0

    Robot() {
        $this.Reset()
    }

    hidden static [void] EnsurePool() {
        if ([Robot]::Pool.Count -gt 0) { return }

        # Build all possible names (26*26*1000 = 676,000)
        $all = foreach ($l1 in 'A'..'Z') {
            foreach ($l2 in 'A'..'Z') {
                for ($n = 0; $n -le 999; $n++) {
                    "{0}{1}{2:d3}" -f $l1, $l2, $n
                }
            }
        }

        # Shuffle once to avoid predictable sequences
        [Robot]::Pool = @($all | Get-Random -Shuffle)
        [Robot]::Index = 0
    }

    [void] Reset() {
        [Robot]::EnsurePool()

        if ([Robot]::Index -ge [Robot]::Pool.Length) {
            throw "No more unique robot names available."
        }

        $this.Name = [Robot]::Pool[[Robot]::Index]
        [Robot]::Index++
    }
}
