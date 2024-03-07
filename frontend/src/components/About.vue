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
                I am a passionate and motivated software developer proficient in languages and
                technologies such as Python, TypeScript, Javascript, React, Vue, Django, and more.
                Creating infastructure and backend solutions is very satisfying to me, and I am
                always looking for new ways to improve my skills and learn the latest technologies.
              </p>
              <br />
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
                I have worked in food service for many years, including a team management position
                as a Shift Lead at Starbucks. I have been hard at work learning and improving my
                skills as a developer, and I am excited to bring my passion for technology and
                problem solving to a new career in software development.
              </p>
              <br />
              <p>
                When programming, I enjoy identifying and overcoming challenges, and making
                meaningful contributions to projects that improve lives or simply bring joy.
              </p>
              <p>
                Beyond the computer, I have a passion for music, watching sports, and keeping up
                with updates in technology and science.
              </p>
            </div>
          </div>
        </div>
        <div class="listDiv" id="bottom">
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
            </ul>
          </div>
        </div>
      </div>
      <br />
      <div class="containerRight">
        <div class="list">
          <h3 class="listHead">Skills</h3>
          <div id="rightList">
            <ul>
              <li>Programming Languages</li>
              <ul>
                <li>Python</li>
                <li>Typescript</li>
                <li>JavaScript</li>
                <li>C</li>
              </ul>
              <li>Frameworks and Libraries</li>
              <ul>
                <li>React</li>
                <li>Vue</li>
                <li>Django</li>
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
                <li>Team Management</li>
                <li>Communication</li>
              </ul>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.listHead {
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
  min-height: 100vh;
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
  justify-content: center;
  width: 75%;
}

.containerRight {
  display: flex;
  flex-direction: column;
}
.containerLeft {
  display: flex;
  flex-direction: column;
  width: 75%;
  margin-right: 1rem;
}

.listDiv {
  height: fit-content;
}

#top {
  margin-bottom: 1rem;
}
#bottom {
  height: 100%;
}
#rightList {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 85%;
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

@media (max-width: 768px) {
  #aboutContainer {
    padding: 0 1rem 0;
  }

  .listContainer {
    flex-direction: column;
    width: 100%;
    align-items: center;
  }

  .containerLeft {
    width: 100%;
    margin-right: 0;
  }
  .containerRight {
    width: 100%;
    padding-top: 1rem;
  }
}
</style>
