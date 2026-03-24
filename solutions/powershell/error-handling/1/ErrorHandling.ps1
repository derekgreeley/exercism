function NonTerminationError {
    Write-Error "Error: This is a non termination error"
}

function ValueErrorHandling {
    param(
        $Age
    )

    try {
        $parsedAge = [int]$Age

        if ($parsedAge -lt 18) {
            throw "Error: Age need to be 18 and up"
        }

        return "I'm $parsedAge years old!"
    }
    catch {
        return "Error: Age need to be 18 and up"
    }
}

function TypedErrorHandling {
    param(
        [string]$Path
    )

    try {
        Get-Content -Path $Path -ErrorAction Stop | Out-Null
    }
    catch {
        $message = $_.Exception.Message

        if ($message -like "*Cannot find path*because it does not exist*") {
            return "Error: File not found"
        }

        if ($message -like "*path*too long*") {
            return "The specified file name or path is too long, or a component of the specified path is too long."
        }

        return $message
    }
}

function ReThrowErrorHandling {
    try {
        throw "Error: Path wasn't provided."
    }
    catch {
        throw
    }
}