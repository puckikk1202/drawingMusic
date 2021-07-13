from scipy.io.wavfile import write
import numpy as np

import pickle

samplerate = 44100

def get_piano_notes():
    '''
    Returns a dict object for all the piano 
    note's frequencies
    '''
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 261.63 #Frequency of Note C4
    
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
    note_freqs[''] = 0.0
    
    return note_freqs
    
def get_wave(freq, duration=0.5):
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave
    
    
def get_song_data(music_notes):
    note_freqs = get_piano_notes()
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song.astype(np.int16)
    
def get_chord_data(chords):
    chords = chords.split('-')
    note_freqs = get_piano_notes()
    
    chord_data = []
    for chord in chords:
        data = sum([get_wave(note_freqs[note]) for note in list(chord)])
        chord_data.append(data)
    
    chord_data = np.concatenate(chord_data, axis=0)    
    return chord_data.astype(np.int16)


def writenote(notes):
    mynote = []
    note_dict = {12 :'C', 
                 11 :'c', 
                 10 :'D', 
                 9 :'d', 
                 8 :'E', 
                 7 :'F', 
                 6 :'f', 
                 5 :'G', 
                 4 :'g', 
                 3 :'A', 
                 2 :'a', 
                 1 :'B'}
    print(notes)
    for num in notes:
        mynote.append(note_dict[num])
    mysong = str(mynote[0]+'-'+
                 mynote[1]+'-'+
                 mynote[2]+'-'+
                 mynote[3]+'-'+
                 mynote[4]+'-'+
                 mynote[5]+'-'+
                 mynote[6]+'-'+
                 mynote[7]+'--'+

                 mynote[8]+'-'+
                 mynote[9]+'-'+
                 mynote[10]+'-'+
                 mynote[11]+'-'+
                 mynote[12]+'-'+
                 mynote[13]+'-'+
                 mynote[14]+'-'+
                 mynote[15]+'--'+
                 
                 mynote[0]+'-'+
                 mynote[3]+'-'+
                 mynote[2]+'-'+
                 mynote[3]+'-'+
                 mynote[4]+'-'+
                 mynote[5]+'-'+
                 mynote[5]+'-'+
                 mynote[7]+'--'+
                 
                 mynote[8]+'-'+
                 mynote[11]+'-'+
                 mynote[10]+'-'+
                 mynote[9]+'-'+
                 mynote[12]+'-'+
                 mynote[14]+'-'+
                 mynote[13]+'-'+
                 mynote[15])
    # mysong = str(mynote[0]+
    #              mynote[1]+
    #              mynote[2]+
    #              mynote[3]+
    #              mynote[4]+
    #              mynote[5]+
    #              mynote[6]+
    #              mynote[7]+'-'+

    #              mynote[8]+
    #              mynote[9]+
    #              mynote[10]+
    #              mynote[11]+
    #              mynote[12]+
    #              mynote[13]+
    #              mynote[14]+
    #              mynote[15]+'-'+
                 
    #              mynote[0]+
    #              mynote[3]+
    #              mynote[2]+
    #              mynote[3]+
    #              mynote[4]+
    #              mynote[5]+
    #              mynote[5]+
    #              mynote[7]+'-'+
                 
    #              mynote[8]+
    #              mynote[11]+
    #              mynote[10]+
    #              mynote[9]+
    #              mynote[12]+
    #              mynote[14]+
    #              mynote[13]+
    #              mynote[15])
    print(mysong)    
    data = get_song_data(mysong)
    data = data * (16300/np.max(data))
    write('mysong.wav', samplerate, data.astype(np.int16))

    #Notes of "twinkle twinkle little star"
    '''
    music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C'
    data = get_song_data(music_notes)
    data = data * (16300/np.max(data))
    write('twinkle-twinkle.wav', samplerate, data.astype(np.int16))
    
    #Playing chords
    chords = 'EgB-DfA-AcE-BDf-gAcE-fAc'
    data = get_chord_data(chords)
    data = data * (16300/np.max(data))
    data = np.resize(data, (len(data)*5,))
    write('exp-C-Major.wav', samplerate, data.astype(np.int16))
    '''
# if __name__=='__main__':
#     main()
