import click
import can
import cantools

CAN_FILE_EXTENSION = ["asc","blf","csv","db","log","txt"]
CANT_FILE_EXTENSION = ["dbc", "kcd", "sym", "arxml", "cdd"]

def loadfile(input_file, filter_by, filter_for):
    db = cantools.database.load_file(input_file)
    if filter_by == "name":
        message = db.get_message_by_name(filter_for)
        return(message)
    elif filter_by == "id":
        message = db.get_message_by_frame_id(int(filter_for,16))
        return(message)
    else: return(db)

@click.group()
def cli():pass

@cli.command()
@click.argument("input-file", type=click.Path())
@click.argument("output-file")
@click.option("-b", "--filter-by", help='filter by arbitration ID')
@click.option("-f", "--filter-for", help='filter by name')
@click.option("-v", "--verbose", help='prints to stdout', is_flag=True)

def tofile(input_file, output_file, filter_by, filter_for, verbose):
    '''
    'convert tofile'  Converts input file to a different format and writes to output

    input-file      the database input file                               
    output-file     the output for the converted database file
    '''
    db = loadfile(input_file, filter_by, filter_for)
    if verbose == True: print(db)
    cantools.database.dump_file(db, output_file)
    print(f"Database written to {output_file}")
    pass

#@cli.command()

#def tobus():
#    '''
#    'convert tobus'  Converts input file and sends it through the injector module
#    '''
#    pass