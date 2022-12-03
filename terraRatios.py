
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

    return [ index for index in range( numOfTypes ) if 0.0 < typing[ index ] < 1.0 ]

def calcStrengths( type1, type2, typeChart ):

    numOfTypes = getTypeNum( typeChart )

    typing = calcTyping( type1, type2, typeChart )

    return [ index for index in range( numOfTypes ) if typing[ index ] > 1.0 ]

def calcImmunities( type1, type2, typeChart ):

    numOfTypes = getTypeNum( typeChart )

    typing = calcTyping( type1, type2, typeChart )

    return [ index for index in range( numOfTypes ) if typing[ index ] == 0.0 ]

def offensiveCalculations(  type1, type2, typeChart ):

    strengths = ( calcStrengths( type1, 'none', typeChart ), calcStrengths( type2, 'none', typeChart ) )

    weaknesses = ( calcWeaknesses(  type1, 'none', typeChart ), calcWeaknesses(  type2, 'none', typeChart ) )

    immunities = ( calcImmunities( type1, 'none', typeChart ), calcImmunities( type2, 'none', typeChart ) )

    return { "strength" : strengths, "weakness" : weaknesses, "immunity" : immunities }


def defensiveCalculations(  type1, type2, typeChart ):

    strengths = calcStrengths( type1, type2, typeChart )

    weaknesses = calcWeaknesses(  type1, type2, typeChart )

    immunities = calcImmunities( type1, type2, typeChart )

    return { "immunity" : immunities, "resistant" : weaknesses, "weakness" : strengths }

def displayOffensiveCalcuations( type1, type2, typeChart ):

    types = getTypeNames( typeChart )

    calculations = offensiveCalculations( type1, type2, typeChart )

    kinds = calculations.keys()

    print( "|| Offensive Calculations ||\n" )

    for kind in kinds:
        print( "|", kind.capitalize(), "|" )

        print( "1st Type", kind.capitalize() + ":",  getTypes( calculations[ kind ][ 0 ], types ) )
        if( type2 != 'none' ):
            print( "2nd Type", kind.capitalize() + ":",  getTypes( calculations[ kind ][ 1 ], types ) )
            print( "Dual-Type", kind.capitalize() + ":",  getTypes( calculations[ kind ][ 0 ] + calculations[ kind ][ 1 ], types ) )
        print()

def displayDefensiveCalcuations( type1, type2, typeChart ):

    types = getTypeNames( typeChart )

    calculations = defensiveCalculations( type1, type2, typeChart )

    kinds = calculations.keys()

    print( "|| Defensive Calculations ||\n" )

    for kind in kinds:
        print( "|", kind.capitalize(), "|" )

        if( type1 == "none" or type2 == "none" ):
            print( "Mono-Type", kind.capitalize() + ":",  getTypes( calculations[ kind ], types ) )
        else:
            print( "Dual-Type", kind.capitalize() + ":",  getTypes( calculations[ kind ], types ) )
        print()

def main():

    offTypeChart = importTypeChart( "./typeChart.txt" )

    defTypeChart = convertOffDef( offTypeChart )

    userTypes = [ indType.lower() for indType in ( input( "1st Type: " ), input( "2nd Type: " ), input( "Terra Type: " ) ) ]

    print()
    
    assert all( typeCheck( indType, offTypeChart ) for indType in userTypes )

    #print( "Offensive Type 1:", getTypes( calcStrengths( userTypes[ 0 ], userTypes[ 1 ], offTypeChart ), getTypeNames( offTypeChart ) ) )
    #print( "Offensive Weaknesses:", getTypes( calcWeaknesses( userTypes[ 0 ], userTypes[ 1 ], offTypeChart ), getTypeNames( offTypeChart ) ) )

    #print( "Defensive Strengths:", getTypes( calcWeaknesses( userTypes[ 0 ], userTypes[ 1 ], defTypeChart ), getTypeNames( defTypeChart ) ) )
    #print( "Defensive Weaknesses:", getTypes( calcStrengths( userTypes[ 0 ], userTypes[ 1 ], defTypeChart ), getTypeNames( defTypeChart ) ) )

    displayOffensiveCalcuations( userTypes[ 0 ], userTypes[ 1 ], offTypeChart )
    displayDefensiveCalcuations( userTypes[ 0 ], userTypes[ 1 ], defTypeChart )



main()