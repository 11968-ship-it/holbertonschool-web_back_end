Setup
Install NodeJS 20.x.x
(in your home directory):

curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
$ nodejs -v
v20.15.1
$ npm -v
10.7.0
Install Jest, Babel, and ESLint
in your project directory:

Install Jest using: npm install --save-dev jest
Install Babel using: npm install --save-dev babel-jest @babel/core @babel/preset-env
Install ESLint using: npm install --save-dev eslint
Configuration files
Please create the following 3 files (with the provided contents) in the project directory:

package.json
Click to show/hide file contents
babel.config.js
Click to show/hide file contents
.eslintrc.js
Click to show/hide file contents
Finally…
Don't forget to run npm install from the terminal of your project folder to install all necessary project dependencies. Do not push on your repository the folder node_modules that has been created.

Tasks
0. Const or let?
Modify

function taskFirst to instantiate variables using const
function taskNext to instantiate variables using let
export function taskFirst() {
  var task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  var combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
Execution example:

bob@dylan:~$ cat 0-main.js
import { taskFirst, taskNext } from './0-constants.js';

console.log(`${taskFirst()} ${taskNext()}`);

bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-main.js 
I prefer const when I can. But sometimes let is okay
bob@dylan:~$ 
Repo:

GitHub repository: holbertonschool-web_back_end
Directory: ES6_basic
File: 0-constants.js
