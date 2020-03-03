*** Keywords ***

SELECT ROUTE
    [Arguments]    ${route}
    CHOOSE ROUTE    ${route}
    ${average} =    CALCULATE AVERAGE    ${lst}
    [Return]    ${average}

GENERATE PLOT
    [Arguments]    ${lst1}    ${lst2}    ${lst3}    ${loops}
    PLOT    ${lst1}    ${lst2}    ${lst3}    ${loops}

GET LENGTHS
    ${lengths} =    GET SCREEN LENGTHS
    ${height} =    ${lengths}[0]
    ${width} =    ${lengths}[1]
    [Return]    ${height}    ${width}