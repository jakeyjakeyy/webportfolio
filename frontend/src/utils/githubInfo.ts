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

const GITHUB_KEY = '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' // token with no permissions, hiding the key is the only reason I need to create a backend, so I'm keeping it here for now
async function fetchAndProcessLanguages(url: string, index?: number): Promise<LanguageData> {
  const response = await fetch(url, {
    headers: {
      Authorization: `Bearer ${GITHUB_KEY}`
    }
  })
  const languages: LanguageData = await response.json()
  let totalSize = 0
  for (const size of Object.values(languages)) {
    totalSize += size
  }
  const languagePercentages: LanguageData = {}
  for (const [lang, size] of Object.entries(languages)) {
    languagePercentages[lang] = parseFloat(((size / totalSize) * 100).toFixed(2))
    if (index) {
      languagePercentages[lang] = languagePercentages[lang] / index
    }
  }
  return languagePercentages
}

async function githubInfo(username: string): Promise<UserActivityAndLanguages> {
  if (username != 'jakeyjakeyy') {
    const languagePercentages = await fetchAndProcessLanguages(
      `https://api.github.com/repos/jakeyjakeyy/${username}/languages`
    )
    return {
      lastActive: 'N/A',
      languagePercentages
    }
  }
  const response = await fetch(`https://api.github.com/users/jakeyjakeyy/events/public`, {
    headers: {
      Authorization: `Bearer ${GITHUB_KEY}`
    }
  })
  const events: Array<{ created_at: string }> = await response.json()
  const lastActive = events[0].created_at

  const repoResponse = await fetch(`https://api.github.com/users/jakeyjakeyy/repos`, {
    headers: {
      Authorization: `Bearer ${GITHUB_KEY}`
    }
  })
  const repos: Repo[] = await repoResponse.json()

  const languages: LanguageData = {}
  for (const repo of repos) {
    const langData = await fetchAndProcessLanguages(
      `https://api.github.com/repos/jakeyjakeyy/${repo.name}/languages`,
      Object.keys(repos).length
    )
    for (const [lang, size] of Object.entries(langData)) {
      languages[lang] = (languages[lang] || 0) + size
    }
  }
  return {
    lastActive,
    languagePercentages: languages
  }
}
export default githubInfo
