# Miscellaneous junk I don't want to throw away
import numpy as np
from functools import partial

def single_break(s:int, c:int)->list:
  """
    s: "stick" of integral length, to be broken
    c: minimum distance between breaks
    returns tuple of all possible _numbers_ of breaks, interpreted as breaking
      off a length c from a longer stick
  """
  q,r = divmod(s,c)
  out = list(range(q+1))
  return out

def double_break(s:int, c:int, o:int, q:int)->list:
  sbr = single_break(s-q*o, c)
  return [(q,br) for br in sbr]


def stick_break(s:int, c:int, o:int)->list:
  """
  s: "stick" of integral length, to be broken
  c: minimum distance between 'short-template' breaks
  o: minimum distance between 'long-template' breaks
  returns tuple of all possible _numbers_ of breaks, interpreted as breaking
    off a length o or of length c from a longer stick
  """
  out = []
  if c >= s:
    return [(0,0)]
  elif (c < s) and (s < o):
    csh = single_break(s,c)
    out += [(0,q) for q in csh]
  else:
    osh = single_break(s,o)
    for u in osh:
      out += double_break(s,c,o,u)
  return out


def counterf_ratios(hist, fund_rate, Rstar, s0, o_idx, c_idx, o_cost, c_cost):
    """
    computes 
    """
    revenue = hist*fund_rate
    open_vec = np.zeros(len(hist)) 
    open_vec[o_idx] = 1
    close_vec = np.zeros(len(hist))
    close_vec[c_idx] = 1

    net_vec = open_vec - close_vec

    R_vec = hist / (s0 + np.cumsum(net_vec))
    
    rev_budget = revenue - o_cost*open_vec - c_cost*close_vec
    rev_budget = np.round(np.cumsum(rev_budget))
    
    result_bool = [ (x <= Rstar) for x in R_vec]
    prop = sum(result_bool)/len(result_bool)
    
    out_obj = {'rev_budget': rev_budget,
               'rev_ratios':R_vec,
               'prop':prop
              }
    
    return out_obj


def cr_to_optimize(hist, fund_rate, Rstar, s0, o_idx, c_idx, o_cost, c_cost):
    return 1-counterf_ratios(hist, fund_rate, Rstar, s0, o_idx, c_idx, o_cost, c_cost)['prop']


def optim_funcs(hist, fund_rate, Rstar, s0, n_o, n_c, o_cost, c_cost):
    local_or = partial(hist=hist, fund_rate=fund_rate, Rstar=Rstar, s0=s0,  c_idx=[], o_cost=o_cost, c_cost = c_cost)
    local_cr = partial(hist=hist, fund_rate=fund_rate, Rstar=Rstar, s0=s0,  o_idx=[], o_cost=o_cost, c_cost = c_cost)

    single_or = lambda x: local_or(o_idx=[x])
    single_cr = lambda x: local_cr(c_idx=[x])
    o_lb = np.argmin(abs(total_revenue + o_cost))
    c_lb = np.argmin(abs(total_revenue - c_cost))
    out_dict = {
        'local_or':local_or,
        'local_cr':local_cr,
        'single_or':single_or,
        'single_cr':single_cr,
        'o_lb':o_lb,
        'c_lb':c_lb
    }
    return out_dict


def optim_loop(hist, fund_rate, Rstar, s0, n_o, n_c, o_cost, c_cost):
    funcs = optim_funcs(hist=hist, fund_rate=fund_rate, Rstar=Rstar, s0=s0,  n_o=n_o, n_c=n_c, o_cost=o_cost, c_cost = c_cost)
    o_idxs = []
    c_idxs = []
    # establish baseline ratio
    base_curve = [funcs['single_or'](x) for x in range(funcs['c_lb'], len(hist))]
    baseline = min(base_curve)
    base_idx = funcs['c_lb'] + np.argmin(base_curve)
    o_idxs.append(base_idx)
    test_base = baseline - 1.
    counter_results = counterf_ratios(hist=hist, fund_rate=fund_rate, Rstar=Rstar, s0=s0, o_idx=o_idxs, c_idx=[], o_cost=o_cost, c_cost = c_cost)
    while test_base <= baseline:
        newfuncs = optim_funcs(hist=hist, fund_rate=fund_rate, Rstar=Rstar, s0=s0,  n_o=n_o, n_c=n_c, o_cost=o_cost, c_cost = c_cost)
      
        # establish baseline ratio
        rev_curve = [funcs['single_or'](x) for x in range(funcs['c_lb'], len(hist))]
        test_base = min(rev_curve)
        rev_idx = funcs['c_lb'] + np.argmin(base_curve)
        
    
    return 