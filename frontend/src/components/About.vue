<script setup lang="ts"></script>

<template>
  <div id="aboutContainer">
    <h2>About Jake</h2>
    <div class="listContainer">
      <div class="containerLeft">
        <div class="listDiv" id="top">
          <div class="list">
            <h3 class="listHead">About</h3>
            <div class="about">
              <p>
                I am a passionate and motivated software developer proficient in technologies such
                as Python, JavaScript, React, Vue, Django, and more. Creating infastructure and
                backend solutions is very satisfying, and I am always looking for new ways to
                improve my skills and learn new technologies.
              </p>
              <p>
                The opportunity to constantly learn and improve my skills as a developer drives me
                every day, and I am proud to hold certificates from Harvard's CS50 in both
                <a
                  href="https://certificates.cs50.io/88d1f811-c6f5-4bb9-9411-acbea8dae793.pdf?size=letter"
                >
                  Web Programming with Python and JavaScript</a
                >, and
                <a
                  href="https://certificates.cs50.io/5e16f81f-9ee8-458c-b73a-4c89f53a5321.pdf?size=letter"
                  >Introduction to Computer Science</a
                >.
              </p>
              <br />
              <p>
                When programming, I enjoy identifying and overcoming challenges, and making
                meaningful contributions to projects that improve lives or bring joy.
              </p>
              <p>
                Beyond the computer, I have a passion for music, watching sports (go Warriors! 🏀),
                and keeping up with technology and science.
              </p>
            </div>
          </div>
        </div>
        <div class="listDiv">
          <div class="list">
            <h3 class="listHead">Certifications and Education</h3>
            <ul>
              <li>HarvardX</li>
              <ul>
                <li>Dates Attended</li>
                <ul>
                  <li>2023</li>
                </ul>
                <li>Degree</li>
                <ul>
                  <li>Certificate in Web Programming with Python and JavaScript</li>
                  <li>Certificate in Introduction to Computer Science</li>
                </ul>
              </ul>
              <li>Live Oak</li>
              <ul>
                <li>Dates Attended</li>
                <ul>
                  <li>2012-2016</li>
                </ul>
                <li>Degree</li>
                <ul>
                  <li>High School Diploma</li>
                </ul>
              </ul>
            </ul>
          </div>
        </div>
      </div>
      <br />
      <div class="containerRight">
        <div class="list">
          <h3 class="listHead">Skills</h3>
          <ul>
            <li>Programming Languages</li>
            <ul>
              <li>Python</li>
              <li>JavaScript</li>
              <li>C</li>
            </ul>
            <li>Frameworks and Libraries</li>
            <ul>
              <li>React</li>
              <li>Vue</li>
              <li>Django</li>
              <li>Bootstrap</li>
            </ul>
            <li>Tools</li>
            <ul>
              <li>Git</li>
              <li>GitHub</li>
              <li>Docker</li>
              <li>VS Code</li>
            </ul>
            <li>Database Management Systems</li>
            <ul>
              <li>SQL</li>
              <li>Postgres</li>
              <li>Other relational databases</li>
            </ul>
            <li>Operating Systems</li>
            <ul>
              <li>Linux</li>
              <li>Windows</li>
            </ul>
            <li>Proficiencies</li>
            <ul>
              <li>Problem Solving</li>
              <li>Working with a team</li>
              <li>Communication</li>
            </ul>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h3 {
  margin-bottom: 1rem;
  align-self: flex-start;
}
ul {
  padding-left: 1rem;
}
#aboutContainer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: var(--color-background);
  padding: 0 3rem 0;
}

.about {
  border-radius: 1rem;
  padding: 1rem;
  background-color: var(--color-background);
}

.listContainer {
  display: flex;
  flex-direction: row;
  padding: 1rem;
  border-radius: 1rem;
}

.containerLeft,
.containerRight {
  display: flex;
  flex-direction: column;
}
.containerLeft {
  width: 85%;
  margin-right: 1rem;
}

.listDiv {
  height: fit-content;
}

#top {
  margin-bottom: 1rem;
}

.list {
  background-color: var(--color-background-soft);
  border-radius: 1rem;
  padding: 1rem;
  height: 100%;
  width: 100%;
}

.listHead {
  color: var(--color-accent);
}
</style>
