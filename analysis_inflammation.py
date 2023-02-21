import numpy as np
import matplotlib.pyplot as plt
import glob

def visualize(f):
    """Plot maximum, minimum and mean values of two dimensional data.
    
    Plot maximum, minimum and mean values calculated across all rows of 
    data contained in a CSV file, and save plot in a PNG file.
    
    Parameters
    ----------
    f : str
        name (including path) of CSV file containing the data.
    
    Returns
    -------
    None
    
    Raises
    ------
    None
    
    """
    data = np.loadtxt(f, delimiter=',')
    
    fig = plt.figure(figsize=(10, 3))
    
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)
    
    axes1.plot(data.max(axis=0), '-o', color='red')
    axes2.plot(data.min(axis=0), '-o', color='blue')
    axes3.plot(data.mean(axis=0), '-o', color='green')
    
    for ax in fig.get_axes():
        ax.set_xlabel('Days')

    axes1.set_ylabel('Maximum')
    axes2.set_ylabel('Minimum')
    axes3.set_ylabel('Mean')
    
    fig.tight_layout()
    plt.savefig(f[:-3] + 'png')
    plt.show()


def detect_zero_minima(f, output_f):
    """Flag behaviour in minimum values of two dimensional data.
    
    The flagged behaviour corresponds to the sum of the minimum values
    observed across all rows of two dimensional data read from a CSV file.
    If the sum is zero, print the name of the file to the screen and list
    it in an output file object provided as input.
    
    Parameters
    ----------
    f: str
        name (including path) of CSV file containing the data
    output_f: file obj
        file object where the flagged files will be listed
        
    Returns
    -------
    None
    
    Raises
    ------
    None
    
    """
    data = np.loadtxt(f, delimiter=',')
    
    if np.sum(data.min(axis=0)) == 0:
        print('Minima adds up to zero for file: ', f)
        output_f.write(f + '\n')
        
    print('\nContinuing\n')

if __name__ == '__main__':
    print('Using analysis_inflammation as source file')
    print(__name__)