
Function Invoke-Sieve {
    <#
    .SYNOPSIS
        Find all prime numbers up to an inclusive limit.

    .DESCRIPTION
        Implements the Sieve of Eratosthenes by marking
        multiples of prime numbers as composite.

    .PARAMETER Limit
        The inclusive upper limit for finding primes.

    .EXAMPLE
        Invoke-Sieve -Limit 10
        Returns: @(2, 3, 5, 7)
    #>

    [CmdletBinding()]
    Param(
        [int]$Limit
    )

    # No prime numbers exist below 2
    if ($Limit -lt 2) {
        return @()
    }

    # Create an array to track prime candidates
    $isPrime = [bool[]]::new($Limit + 1)

    # Initially assume all numbers >= 2 are prime
    for ($i = 2; $i -le $Limit; $i++) {
        $isPrime[$i] = $true
    }

    # Mark composite numbers
    for ($p = 2; $p * $p -le $Limit; $p++) {

        if ($isPrime[$p]) {

            # Start at p squared because smaller
            # multiples have already been marked
            for ($multiple = $p * $p;
                 $multiple -le $Limit;
                 $multiple += $p) {

                $isPrime[$multiple] = $false
            }
        }
    }

    # Collect all remaining prime numbers
    $primes = @()

    for ($i = 2; $i -le $Limit; $i++) {
        if ($isPrime[$i]) {
            $primes += $i
        }
    }

    return $primes
}
