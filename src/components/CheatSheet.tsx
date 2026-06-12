import { useState } from 'react';
import { usePyodide } from '../hooks/usePyodide';
import { 
  Code, Terminal, Play, Clipboard, CheckCircle, Search, 
  Layers
} from 'lucide-react';

interface CheatSheetItem {
  category: string;
  title: string;
  description: string;
  code: string;
}

export default function CheatSheet() {
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [selectedItem, setSelectedItem] = useState<CheatSheetItem | null>(null);
  const [consoleLogs, setConsoleLogs] = useState<any[]>([]);
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const { loading: pyodideLoading, runCode } = usePyodide();

  const cheatSheetItems: CheatSheetItem[] = [
    {
      category: 'Syntax Basics',
      title: 'Variables & Data Types',
      description: 'Declaration of string, integer, float, and boolean variables with label printing.',
      code: `name = "Alex"
age = 20
height = 5.9
is_developer = True

print(f"Name: {name}, Age: {age}, Height: {height}, Developer: {is_developer}")
print(f"Data types: {type(name)}, {type(age)}, {type(height)}, {type(is_developer)}")`
    },
    {
      category: 'Data Structures',
      title: 'List Methods',
      description: 'Manipulating lists using append, pop, sort, and slice notation.',
      code: `fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Appended orange:", fruits)

last_fruit = fruits.pop()
print("Popped item:", last_fruit)
print("Updated list:", fruits)

fruits.sort()
print("Sorted list:", fruits)`
    },
    {
      category: 'Data Structures',
      title: 'Dictionary Operations',
      description: 'Accessing and updating key-value pairs using get(), keys(), and items().',
      code: `student = {
    "name": "Alex",
    "age": 20,
    "major": "Computer Science"
}

print("Name:", student.get("name"))
print("All Keys:", list(student.keys()))

student["age"] = 21
print("Updated dict:", student)`
    },
    {
      category: 'Control Flow',
      title: 'Loops and Enumeration',
      description: 'Iterating through sequences using standard for-loops and the enumerate function.',
      code: `languages = ["Python", "JavaScript", "C++"]

for index, lang in enumerate(languages, start=1):
    print(f"Language #{index}: {lang}")`
    },
    {
      category: 'Object-Oriented Programming',
      title: 'Classes and Inheritance',
      description: 'Declaring classes, constructor initialization, method overriding, and inheritance.',
      code: `class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

my_dog = Dog("Buddy")
print(f"{my_dog.name} says {my_dog.speak()}")`
    },
    {
      category: 'Advanced Python',
      title: 'Decorators',
      description: 'Wrapping a function with another function using decorators to extend its execution.',
      code: `def my_decorator(func):
    def wrapper():
        print("[System] Action Starting...")
        func()
        print("[System] Action Finished!")
    return wrapper

@my_decorator
def greet():
    print("Hello from greet function!")

greet()`
    },
    {
      category: 'Advanced Python',
      title: 'Generators & Yield',
      description: 'Creating a custom memory-efficient iterator utilizing the yield statement.',
      code: `def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(3):
    print(f"Countdown: {number}")`
    }
  ];

  const handleCopy = (codeText: string, index: number) => {
    navigator.clipboard.writeText(codeText);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  const handleRunExample = async (item: CheatSheetItem) => {
    setSelectedItem(item);
    setIsRunning(true);
    setConsoleLogs([
      { type: 'system', text: `Initializing code compiler...` },
      { type: 'system', text: `> python example.py` }
    ]);

    const stdoutCallback = (text: string) => {
      setConsoleLogs(prev => [...prev, { type: 'stdout', text }]);
    };

    const stderrCallback = (text: string) => {
      setConsoleLogs(prev => [...prev, { type: 'stderr', text }]);
    };

    const result = await runCode(item.code, stdoutCallback, stderrCallback);
    
    if (result.success) {
      setConsoleLogs(prev => [
        ...prev,
        { type: 'system', text: `Finished script execution.` }
      ]);
    } else {
      setConsoleLogs(prev => [
        ...prev,
        { type: 'stderr', text: result.error || 'SyntaxError' }
      ]);
    }
    setIsRunning(false);
  };

  const filteredItems = cheatSheetItems.filter(item => 
    item.title.toLowerCase().includes(searchTerm.toLowerCase()) || 
    item.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
    item.category.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="space-y-8 animate-fade-in pb-12 relative z-10">
      
      {/* Page Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-extrabold text-white tracking-tight flex items-center gap-2">
            <Layers className="w-6 h-6 text-sky-400" />
            Python Syntax & Concepts Cheat Sheet
          </h1>
          <p className="text-xs text-slate-400 mt-1">Quick-reference syntax cards with interactive compilers. Copy code or run it live in the browser.</p>
        </div>

        {/* Search bar */}
        <div className="relative w-full md:w-80">
          <Search className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search syntax, loops, OOP..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-10 pr-4 py-2 text-xs font-semibold rounded-xl border border-white/5 bg-slate-900/40 text-white placeholder-slate-500 focus:outline-none focus:border-sky-500 transition-colors"
          />
        </div>
      </div>

      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6 items-start">
        
        {/* Left Side: Cards Grid */}
        <div className="xl:col-span-2 space-y-4">
          {filteredItems.map((item, index) => (
            <div 
              key={index}
              className="p-6 rounded-xl border border-white/5 bg-slate-900/40 hover:border-white/10 transition-all duration-200 space-y-4"
            >
              <div className="flex justify-between items-start">
                <div>
                  <span className="text-[10px] font-bold text-sky-400 bg-sky-950/60 border border-sky-900/40 px-2 py-0.5 rounded uppercase font-mono">
                    {item.category}
                  </span>
                  <h3 className="text-base font-bold text-slate-100 mt-2">{item.title}</h3>
                  <p className="text-xs text-slate-400 mt-1">{item.description}</p>
                </div>
                
                <div className="flex items-center gap-2">
                  <button
                    onClick={() => handleCopy(item.code, index)}
                    className="p-2 rounded-lg bg-slate-950/40 border border-white/5 text-slate-400 hover:text-white transition-colors"
                    title="Copy code to clipboard"
                  >
                    {copiedIndex === index ? (
                      <CheckCircle className="w-4 h-4 text-emerald-400" />
                    ) : (
                      <Clipboard className="w-4 h-4" />
                    )}
                  </button>
                  <button
                    onClick={() => handleRunExample(item)}
                    className="p-2 rounded-lg bg-sky-500/10 border border-sky-500/20 text-sky-300 hover:bg-sky-500/20 transition-all flex items-center gap-1.5 text-xs font-semibold"
                    title="Run example code in sidebar terminal"
                  >
                    <Play className="w-3.5 h-3.5 fill-current" />
                    Run Code
                  </button>
                </div>
              </div>

              <div className="bg-slate-950/60 p-4 rounded-lg border border-white/5 overflow-x-auto font-mono text-xs text-slate-300 whitespace-pre">
                {item.code}
              </div>
            </div>
          ))}
          
          {filteredItems.length === 0 && (
            <div className="text-center py-12 border border-dashed border-white/5 rounded-xl text-slate-500">
              No matching syntax cards found for "{searchTerm}".
            </div>
          )}
        </div>

        {/* Right Side: Interactive Console for examples */}
        <div className="xl:col-span-1 rounded-xl border border-white/5 bg-slate-900/60 backdrop-blur-xl overflow-hidden sticky top-24">
          <div className="p-4 border-b border-white/5 bg-[#0d1322] flex justify-between items-center">
            <h3 className="text-xs font-bold text-slate-300 uppercase tracking-widest flex items-center gap-2">
              <Terminal className="w-4 h-4 text-amber-500" />
              Example Terminal
            </h3>
            <button
              onClick={() => setConsoleLogs([])}
              className="text-[10px] text-slate-500 hover:text-slate-300 transition-colors"
            >
              Clear
            </button>
          </div>

          <div className="p-4 min-h-[300px] max-h-[450px] overflow-y-auto bg-[#05080e] font-mono text-xs space-y-1">
            {selectedItem && (
              <div className="text-indigo-400 font-bold mb-2 flex items-center gap-1">
                <Code className="w-3.5 h-3.5" />
                Active Sandbox: {selectedItem.title}
              </div>
            )}
            
            {pyodideLoading && (
              <div className="text-sky-400 animate-pulse">Loading WebAssembly Python compiler...</div>
            )}
            
            {!selectedItem && (
              <div className="text-slate-600 italic">
                Terminal idle. Click "Run Code" on any card to view stdout here in real-time.
              </div>
            )}

            {consoleLogs.map((log, index) => {
              if (log.type === 'system') {
                return <div key={index} className="text-slate-500 font-semibold">{log.text}</div>;
              }
              if (log.type === 'stderr') {
                return <div key={index} className="text-red-400 bg-red-950/20 px-2 py-0.5 rounded border border-red-900/30">{log.text}</div>;
              }
              return <div key={index} className="text-slate-200">{log.text}</div>;
            })}
          </div>

          {selectedItem && (
            <div className="p-3 bg-[#0d1322] border-t border-white/5 flex justify-between items-center text-[10px] text-slate-500">
              <span>Python 3.11 WASM Runtime</span>
              <button 
                onClick={() => handleRunExample(selectedItem)}
                disabled={isRunning}
                className="text-sky-400 hover:text-sky-300 transition-colors font-semibold"
              >
                Rerun example
              </button>
            </div>
          )}
        </div>

      </div>

    </div>
  );
}
