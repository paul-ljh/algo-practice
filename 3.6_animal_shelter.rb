load '3_queue.rb'

class Animal
  attr_reader :type, :arrival
  def initialize(type)
    @type = type
    @arrival = Time.now.to_i
  end
end

class AnimalShelter
  def initialize
    @dogs, @cats, @others = Queue.new, Queue.new, Queue.new
  end

  def dequeue_any
    cat, dog, other = [@cats, @dogs, @others].map { |q| q.is_empty? ? -1 : q.peek.arrival }
    case [cat, dog, other].reject { |i| i == -1 }.min
    when nil
      raise 'no animal whatsoever'
    when cat
      return dequeue_cat
    when dog
      return dequeue_dog
    when other
      return @others.pop
    end
  end

  def dequeue_cat
    return @cats.pop
  end

  def dequeue_dog
    return @dogs.pop
  end

  def enqueue(animal_type)
    animal = Animal.new(animal_type)
    case animal_type
    when "dog"
      @dogs.push(animal)
    when "cat"
      @cats.push(animal)
    else
      @others.push(animal)
    end
  end
end

