# Function to get the color code (numeric value) for a resistor color
Function Get-ColorCode {
    <#
    .SYNOPSIS
    Lookup the numeric value associated with a resistor color.

    .DESCRIPTION
    Given a color, return the corresponding numeric value according to the resistor color code.

    .PARAMETER Color
    The color of the resistor band.

    .EXAMPLE
    Get-ColorCode -Color "red"
    Returns: 2
    #>

    [CmdletBinding()]
    Param(
        [string]$Color
    )

    # Resistor color code array based on the mnemonic: Better Be Right Or Your Great Big Values Go Wrong.
    $colorCodes = @(
        "black",  # 0
        "brown",  # 1
        "red",    # 2
        "orange", # 3
        "yellow", # 4
        "green",  # 5
        "blue",   # 6
        "violet", # 7
        "grey",   # 8
        "white"   # 9
    )

    # Convert the color to lowercase to handle case insensitivity
    $Color = $Color.ToLower()

    # Find the index of the color in the colorCodes array
    $index = $colorCodes.IndexOf($Color)

    # Check if the color exists in the array
    if ($index -ge 0) {
        return $index
    }
    else {
        Throw "Invalid color name provided. Please provide a valid resistor color."
    }
}

# Function to get the list of all resistor colors
Function Get-Colors {
    <#
    .SYNOPSIS
    List all the available resistor color bands.

    .DESCRIPTION
    This function returns all the colors available in the resistor color code.

    .EXAMPLE
    Get-Colors
    #>

    # Resistor color code array based on the mnemonic: Better Be Right Or Your Great Big Values Go Wrong.
    $colorCodes = @(
        "black",  # 0
        "brown",  # 1
        "red",    # 2
        "orange", # 3
        "yellow", # 4
        "green",  # 5
        "blue",   # 6
        "violet", # 7
        "grey",   # 8
        "white"   # 9
    )

    # Return all the color codes
    return $colorCodes
}
