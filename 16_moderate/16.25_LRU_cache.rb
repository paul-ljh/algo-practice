load '../2_linked_lists/doubly_linked_list.rb'
require 'pp'

class LRUCache
  attr_accessor :dict, :list

  def initialize(max_size)
    @max_size = max_size
    @dict, @list = Hash.new, DoublyLinkedList.new
  end

  def insert(key, value)
    if @dict.has_key?(key)
      @list.delete(@dict[key])
    elsif @dict.size == @max_size
      deleted = @list.pop
      @dict.delete(deleted.key)
    end
    @dict[key] = @list.add(data: value, key: key)
  end

  def retrieve(key)
    if @dict.has_key?(key)
      deleted = @list.delete(@dict[key])
      @list.add(data: deleted.data, key: deleted.key)
      return deleted.data
    else
      raise "ABSENT KEY"
    end
  end

  def print
    for item in @dict do
      puts "#{item[0]} => (Key: #{item[-1].key}, Value: #{item[-1].data})"
    end
    puts "#{@list.print}"
    puts
  end
end

def test
  c = LRUCache.new(3)
  puts "INIT:"
  c.print
  
  puts "ADDED 3 KEYS:"
  c.insert(:first, 1)
  c.insert(:second, 2)
  c.insert(:third, 3)
  c.print
  
  puts "RETRIEVED :first:"
  c.retrieve(:first)
  c.print
  
  puts "RETRIEVED :third:"
  c.retrieve(:third)
  c.print
  
  puts "INSERTED (second, changed):"
  c.insert(:second, "changed")
  c.print
  
  puts "INSERTED (:forth, 4):"
  c.insert(:forth, 4)
  c.print
  
  begin
    c.retrieve(:random)
  rescue
    puts "ERROR: RETRIVED an invalid key"
  end
end

