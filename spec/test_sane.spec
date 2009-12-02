require File.dirname(File.expand_path __FILE__) + '/../lib/sane'

require 'rubygems' if RUBY_VERSION < '1.9'
require 'spec/autorun'

describe Sane do

  before do
    #Object.send(:remove_const, 'Klass') rescue nil
  end

  it "should have working __DIR__" do
    __DIR__.should_not == nil
  end

  it "should write to files" do
   filename = __DIR__ + '/test'
   File.write(filename, "abc\n")
   assert(File.exist?(filename))
   if RUBY_PLATFORM =~ /mswin|mingw/
     assert(File.binread(filename) == "abc\r\n") # it should have written it out *not* in binary mode
   end
   File.delete filename
  end

  class A
    def go; 3; end
    aliash :go2 => :go
  end

  it "should aliaz right" do
    A.new.go2.should == 3
  end

  it "should have a singleton_class method" do
    class A; end
    A.singleton_class.module_eval { def go; end }
    A.go
  end

  it "should have a binread method" do
    File.open("bin_test", "wb") do |f|; f.write "a\r\n"; end
    assert File.binread("bin_test") == "a\r\n"
  end  

  it "should have a binwrite method" do
   File.binwrite 'bin_test', "a\r\n"
   assert File.binread("bin_test") == "a\r\n"
  end

  it "should hash hashes right" do
    a = {} # this fails in 1.8.6, or works, rather

    a[{:a => 3, :b => 4}] = 3
    assert a[{:b => 4, :a => 3}] == 3
    assert a[{:b => 3, :a => 4}] == nil
    a = {:a => 3}
    a - {:a => 4}
    assert a.length == 1
 
  end

  it "should allow regexes to be added" do
    /a/ + /b/
  end

# my first implementation of this was *awful* LOL
#  it "should allow for brackets on enumerators" do
#    require 'backports' # ugh
#    assert "ab\r\nc".lines[0] == "ab\r\n"
#  end

  it "should have a windows method" do
   require 'rbconfig'
   if RbConfig::CONFIG['host_os'] =~ /mswin|mingw/
      assert OS.windows?
   else
      refute OS.windows?
   end
  end

  it "should have good looking float#inspect" do
     assert(  (1.1 - 0.9).inspect.include? '0.2000000' ) # 0.20000000000000006661 or something close to it
  end

  it "should return false if you call File.executable? non_existent_file" do
    assert !File.executable?('nonexistent')
  end

  it "should have ave method" do
    [1,2,3].ave.should == 2
  end

  it "should have an sputs method that outputs " do
    sputs 1,2,3
  end
   
end
