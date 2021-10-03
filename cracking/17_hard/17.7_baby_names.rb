require 'set'
require 'pp'

class BabeNames
  attr_accessor :names, :synonyms, :syn_hash, :result

  def initialize(names, synonyms)
    @names = names
    @synonyms = synonyms
    @syn_hash = Hash.new
    @result = Hash.new
    group_synonyms()
    combine_frequency()
  end

  def group_synonyms
    for tuple in @synonyms do
      fir, sec = tuple[0], tuple[1]

      # neither exists
      if !@syn_hash.has_key?(fir) && !@syn_hash.has_key?(sec)
        s = Set.new(tuple)
        @syn_hash[fir] = @syn_hash[sec] = s
      
      # both exist
      elsif @syn_hash.has_key?(fir) && @syn_hash.has_key?(sec)
        # both point to diff sets
        if @syn_hash[fir] != @syn_hash[sec]
          if @syn_hash[fir].size > @syn_hash[sec].size
            update(sec, fir)
          else
            update(fir, sec)
          end
        end

      # only one exists
      else
        if @syn_hash.has_key?(fir)
          @syn_hash[fir].add(sec)
          @syn_hash[sec] = @syn_hash[fir]
        else
          @syn_hash[sec].add(fir)
          @syn_hash[fir] = @syn_hash[sec]
        end
      end
    end
  end

  def update(small, big)
    # merge small into big
    @syn_hash[big].merge(@syn_hash[small])

    # update small's keys in hash
    for k in @syn_hash[small] do
      @syn_hash[k] = @syn_hash[big]
    end
  end

  def combine_frequency
    syn_list = @syn_hash.values.uniq
    for syns in syn_list do
      sum = 0
      for name in syns do
        sum += names[name] if names.has_key?(name)
      end
      @result[syns.first] = sum
    end
  end
end

def test
  t1 = BabeNames.new({'a' => 2, 'b' => 3, 'c' => 4, 'e' => 9, 'f' => 10}, [['a', 'b'], ['b', 'c'], ['c', 'd'], ['e', 'f'], ['a', 'f']])
  pp t1.result

  t2 = BabeNames.new({'a' => 2, 'b' => 3, 'c' => 4, 'e' => 9, 'f' => 10, 'g' => 1, 'h' => 1}, [['a', 'b'], ['b', 'c'], ['c', 'd'], ['e', 'f'], ['a', 'f'], ['g', 'h']])
  pp t2.result
end

