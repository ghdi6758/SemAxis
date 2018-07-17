import numpy as np
from scipy import spatial

def cosine_similarity(vec1, vec2):
    return 1.0 - spatial.distance.cosine(vec1, vec2)

def get_avg_vec(emb, word, k):
    tmp = []
    tmp.append(emb.wv[word])
    for closest_word, similarity in emb.most_similar(positive=word, topn=k):
        tmp.append(emb.wv[closest_word])
    avg_vec = np.mean(tmp, axis=0)
    return avg_vec

def transform_antonym_to_axis(emb, antonym, k):
    if k == 0:
        return emb.wv[antonym[1]] - emb.wv[antonym[0]]

    else:
        vec_antonym_1 = get_avg_vec(emb, antonym[1], k)
        vec_antonym_0 = get_avg_vec(emb, antonym[0], k)

        return vec_antonym_1 - vec_antonym_0 

def project_word_on_axis(emb, word, antonym, k=10):
    return cosine_similarity(emb.wv[word], transform_antonym_to_axis(emb, antonym, k)) 


if __name__ == '__main__':

    import gensim
    

    EMBEDDING_PATH = "" ### Yout path to embedding file 

    ######################################################################
    ### Google News embedding (Download: https://code.google.com/archive/p/word2vec/). Note that for SemAxis, bin file needs to be converted to text file: see https://stackoverflow.com/questions/27324292/convert-word2vec-bin-file-to-text)
    
    # test_path = "%s/GoogleNews-vectors-negative300.txt" % (EMBEDDING_PATH)
    ######################################################################

    ######################################################################
    ## Reddit20M embedding (Download: https://drive.google.com/file/d/1ewmS5Uu4tWAkwWsuY8FZVgLr85vvZXye/view?usp=sharing) 

    test_path = "%s/Reddit20M.cbow.300.100.txt" % (EMBEDDING_PATH)
    ######################################################################

    test_embed = gensim.models.KeyedVectors.load_word2vec_format(test_path)
    print(project_word_on_axis(test_embed, "baby", ("hate", "love"), k=3))
    
    ## Test results (with k=3) should be: 
    ## 0.16963434219360352 with Google News embedding
    ## 0.31472429633140564 with Reddit20M embedding

