// move this to backend later to use api key for more information from private repos

interface Repo {
  name: string
}

interface LanguageData {
  [key: string]: number
}

interface UserActivityAndLanguages {
  lastActive: string
  languagePercentages: LanguageData
}

async function githubInfo(username: string): Promise<UserActivityAndLanguages> {
  const response = await fetch(`https://api.github.com/users/${username}/events/public`)
  const events: Array<{ created_at: string }> = await response.json()
  const lastActive = events[0].created_at

  const repoResponse = await fetch(`https://api.github.com/users/${username}/repos`)
  const repos: Repo[] = await repoResponse.json()

  const languages: LanguageData = {}
  let totalSize = 0

  for (const repo of repos) {
    const langResponse = await fetch(
      `https://api.github.com/repos/${username}/${repo.name}/languages`
    )
    const langData: LanguageData = await langResponse.json()

    for (const [lang, size] of Object.entries(langData)) {
      if (languages[lang]) {
        languages[lang] += size
      } else {
        languages[lang] = size
      }
      totalSize += size
    }
  }

  const languagePercentages: LanguageData = {}
  for (const [lang, size] of Object.entries(languages)) {
    languagePercentages[lang] = parseFloat(((size / totalSize) * 100).toFixed(2))
  }

  return {
    lastActive,
    languagePercentages
  }
}
export default githubInfo
