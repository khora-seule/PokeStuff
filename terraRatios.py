
def importTypeChart( path ):

    typeChartRaw = [ line.strip().split() for line in open( path ) ]

    return dict( zip( typeChartRaw[ 0 ], [ [ float( effect ) for effect in typing ] for typing in typeChartRaw[ 1: ] ] ) )

def getTypeNames( typeChart ):

    return list( typeChart.keys() )

def getTypeNum( typeChart ):
    return len( getTypeNames( typeChart ) )


def convertOffDef( typeChart ):

    types = getTypeNames( typeChart )
    numOfTypes = getTypeNum( typeChart )

    return dict( zip( types, [ [ typeChart[ indType1 ][ i ] for indType1 in types ] for i in range( numOfTypes ) ] ) )    


def typeCheck( typing, typeChart ):

    return typing in getTypeNames( typeChart )

def getTypes( indices, types ):

    return [ types[ i ] for i in indices ]

def calcTyping( type1, type2, typeChart ):

    numOfTypes = getTypeNum( typeChart )

    return [ typeChart[ type1 ][ i ] * typeChart[ type2 ][ i ] for i in range( numOfTypes ) ]

def calcWeaknesses( type1, type2, typeChart ):

    numOfTypes = getTypeNum( typeChart )

    typing = calcTyping( type1, type2, typeChart )

    return [ index for index in range( numOfTypes ) if typing[ index ] < 1.0 ]

def calcStrengths( type1, type2, typeChart ):

    numOfTypes = getTypeNum( typeChart )

    typing = calcTyping( type1, type2, typeChart )

    return [ index for index in range( numOfTypes ) if typing[ index ] > 1.0 ]


def main():


    offTypeChart = importTypeChart( "./typeChart.txt" )

    defTypeChart = convertOffDef( offTypeChart )

    userTypes = [ indType.lower() for indType in ( input( "1st Type: " ), input( "2nd Type: " ), input( "Terra Type: " ) ) ]
    
    assert all( typeCheck( indType, offTypeChart ) for indType in userTypes )

    print( "Offensive Strengths:", getTypes( calcStrengths( userTypes[ 0 ], userTypes[ 1 ], offTypeChart ), getTypeNames( offTypeChart ) ) )
    print( "Offensive Weaknesses:", getTypes( calcWeaknesses( userTypes[ 0 ], userTypes[ 1 ], offTypeChart ), getTypeNames( offTypeChart ) ) )

    print( "Defensive Strengths:", getTypes( calcWeaknesses( userTypes[ 0 ], userTypes[ 1 ], defTypeChart ), getTypeNames( defTypeChart ) ) )
    print( "Defensive Weaknesses:", getTypes( calcStrengths( userTypes[ 0 ], userTypes[ 1 ], defTypeChart ), getTypeNames( defTypeChart ) ) )


main()