load "#{Dir.home}/Documents/Interviews/algo-practice/queue.rb"

class Animal
  attr_reader :type, :counter, :name
  VALID_SPECIES = ['cat', 'dog']

  def initialize(name, species, counter)
    @species = species
    @counter = counter
    @name = name
  end
end

class AnimalShelter
  def initialize
    @dogs, @cats = Queue.new, Queue.new
    @counter = 0
  end

  def dequeue_any
    if @dogs.is_empty? && @cats.is_empty?
      raise 'EMPTY QUEUE'
    elsif @dogs.is_empty?
      dequeue_cat()
    elsif @cats.is_empty?
      dequeue_dog()
    else
      @dogs.peek.counter > @cats.peek.counter ? dequeue_cat() : dequeue_dog()
    end
  end

  def dequeue_cat
    @cats.pop.name
  end

  def dequeue_dog
    @dogs.pop.name
  end

  def enqueue(name, species)
    raise 'INVALID SPECIES' unless Animal::VALID_SPECIES.include?(species)
    @counter += 1
    animal = Animal.new(name, species, @counter)
    self.instance_variable_get("@#{species}s").push(animal)
  end
end

def test
  shelter = AnimalShelter.new
  begin
    shelter.dequeue_any
  rescue => e
    puts e.message
    puts    
  end

  begin
    shelter.dequeue_cat
  rescue => e
    puts e.message
    puts    
  end

  begin
    shelter.dequeue_dog
  rescue => e
    puts e.message
    puts    
  end

  begin
    shelter.enqueue('paul', 'human')
  rescue => e
    puts e.message
    puts    
  end

  shelter.enqueue('alice', 'cat')
  shelter.enqueue('bob', 'cat')
  shelter.enqueue('calvin', 'dog')
  
  puts shelter.dequeue_any == 'alice' ? 'PASS' : 'FAIL'
  puts shelter.dequeue_any == 'bob' ? 'PASS' : 'FAIL'
  puts shelter.dequeue_any == 'calvin' ? 'PASS' : 'FAIL'
  begin
    shelter.dequeue_any
  rescue => e
    puts e.message
    puts    
  end
end

