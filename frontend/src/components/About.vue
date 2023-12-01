<script setup lang="ts">
import { onMounted, onUnmounted, reactive } from 'vue';

let listPositions = reactive<Array<{ x: number; y: number }>>([]);

onMounted(() => {
    const listElements = document.querySelectorAll('.list');
    listElements.forEach((list, index) => {
        listPositions[index] = { x: 0, y: 0 };
    });
    window.addEventListener('mousemove', handleMouseMove);
});

onUnmounted(() => {
    window.removeEventListener('mousemove', handleMouseMove);
});

function handleMouseMove(e: MouseEvent) {
    const listElements = document.querySelectorAll('.list');
    listElements.forEach((list, index) => {
        const rect = list.getBoundingClientRect();
        const dx = e.clientX - (rect.left + rect.width / 2);
        const dy = e.clientY - (rect.top + rect.height / 2);
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 100) {
            listPositions[index].x = dx * 0.1;
            listPositions[index].y = dy * 0.1;
        } else {
            listPositions[index].x = 0;
            listPositions[index].y = 0;
        }
    });
}
</script>

<template>
 <div class="aboutContainer">
    <div class="about">
        <p>I am a passionate and motivated software developer with experience in technologies such as Python, JavaScript, React, Vue, and Django.</p>
        <p>The opportunity to constantly learn and improve my skills as a developer drives me every day. I am proud to hold certificates from HarvardX, in both <a href="https://certificates.cs50.io/88d1f811-c6f5-4bb9-9411-acbea8dae793.pdf?size=letter"> Web Programming with Python and JavaScript</a>, and <a href="https://certificates.cs50.io/5e16f81f-9ee8-458c-b73a-4c89f53a5321.pdf?size=letter">Introduction to Computer Science</a>.</p>
        <br>
        <p>When programming, I enjoy creating APIs and backend functionalities, identifying and overcoming challenges, and making meaningful contributions to projects that improve lives or bring joy.</p>
        <p>Beyond coding, I have a strong passion for music, watching sports (go Warriors! 🏀), and keeping up with technology and science.</p>
    </div>
        <br>
    <div class="listContainer">
        <div class="list">
            <ul>
                <h2 class="listHead">Certifications and Education</h2>
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
        </div>
        <br>
        <div class="list">
            <ul>
                <h2 class="listHead">Skills</h2>
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
 </div>
</template>

<style scoped>
.about {
    border: 1px solid var(--color-background-soft);
    border-radius: 1rem;
    padding: 1rem;
    background-color: var(--color-background-soft);
}

.listContainer {
    display: flex;
    flex-direction: row;
    padding: 1rem;
    justify-content: space-between;
    background-color: var(--color-background-soft);
    border: 1px solid var(--color-background-soft);
    border-radius: 1rem;
}

.list {
    background-color: var(--color-background);
    border-radius: 1rem;
    padding: 1rem;
    height: fit-content;
    align-self: center;
}

.listHead {
    color: var(--color-accent);
}
</style>