import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const dbPath = process.argv[2];

    readDatabase(dbPath)
      .then((data) => {
        let response = 'This is the list of our students\n';

        const fields = Object.keys(data).sort((a, b) => a.localeCompare(b));

        fields.forEach((field, index) => {
          const list = data[field];
          response += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
          if (index !== fields.length - 1) response += '\n';
        });

        res.status(200).send(response);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const dbPath = process.argv[2];
    const { major } = req.params;

    // ✅ REQUIRED VALIDATION
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(dbPath)
      .then((data) => {
        const list = data[major] || [];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
