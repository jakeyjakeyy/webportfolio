<script setup lang="ts">
import { ref } from 'vue';
let contentSelection = ref("Home");
</script>

<template>
    <div class="content">
        <div class="selections">
            <button
            tabindex="0"
            @click="contentSelection='Home'" 
            @keyup.enter.space="contentSelection='Home'"
            :class="{active: contentSelection === 'Home'}" class="contentSelectionButton">
            Home
            </button>
            <button
            tabindex="0"
            @click="contentSelection='About'" 
            @keyup.enter.space="contentSelection='About'"
            :class="{active: contentSelection === 'About'}" class="contentSelectionButton">
            About
            </button>
            <button
            tabindex="0"
            @click="contentSelection='Projects'" 
            :class="{active: contentSelection === 'Projects'}" class="contentSelectionButton">
            Projects
            </button>
            <button
            tabindex="0"
            @click="contentSelection='Contact'" 
            :class="{active: contentSelection === 'Contact'}" class="contentSelectionButton">
            Contact
        </button>
        </div>
        <h1>{{ contentSelection }}</h1>
        <div v-if="contentSelection === 'Home'">
            <p>Thanks for vising my web portfolio!</p>
            <p>I'd love to hear from you, click <a href="mailto:jakerichards210@gmail.com">here</a> to send me an email, or view the Contact page to see my other contact information.</p>
        </div>
        <div v-if="contentSelection === 'About'">
            <p>I am a passionate and motivated software developer with experience in technologies such as Python, JavaScript, React, Vue, and Django.</p>
            <p>The opportunity to constantly learn and improve my skills as a developer drives me every day. I am proud to hold certificates from HarvardX, in both <a href="https://certificates.cs50.io/88d1f811-c6f5-4bb9-9411-acbea8dae793.pdf?size=letter"> Web Programming with Python and JavaScript</a>, and <a href="https://certificates.cs50.io/5e16f81f-9ee8-458c-b73a-4c89f53a5321.pdf?size=letter">Introduction to Computer Science</a>.</p>
            <br>
            <p>When programming, I enjoy creating APIs and backend functionalities, identifying and overcoming challenges, and making meaningful contributions to projects that improve lives or bring joy.</p>
            <p>Beyond coding, I have a strong passion for music, watching sports (go Warriors! 🏀), and keeping up with technology and science.</p>
            <br>
            <h2>Certifications and Education</h2>
            <ul>
                <li>HarvardX </li>
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
            <br>
            <h2>Skills</h2>
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
                    <li >SQLite</li>
                    <li>Postgres</li>
                </ul>
                <li>Operating Systems</li>
                <ul>
                    <li>Linux</li>
                    <li>Windows</li>
                </ul>
            </ul>

        </div>  
    </div>
</template>

<style scoped>
.content {
    padding: 1rem 1rem;
    flex: 1 0 auto;
}
.selections {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 1rem;
}
.contentSelectionButton {
    background-color: var(--color-background-soft);
    border: none;
    border-radius: 0.25rem;
    padding: 0.5rem 1rem;
    margin: 0 0.25rem;
    cursor: pointer;
    outline: none;
    font-size: 1rem;
    font-weight: 500;
    color: var(--color-text);
    transition: background-color 0.2s ease-in-out;
}
.contentSelectionButton:hover {
    background-color: var(--color-background);
}

.contentSelectionButton.active {
    background-color: var(--color-accent);
}
</style>