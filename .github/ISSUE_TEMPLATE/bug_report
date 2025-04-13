<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chimera v2.0 Bug Report</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <style>
        .chimera-gradient {
            background: linear-gradient(90deg, #2a3f90 0%, #4c36a1 50%, #7a269e 100%);
        }
        .section-card {
            transition: all 0.3s ease;
            border-left: 4px solid #4c36a1;
        }
        .section-card:hover {
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        body {
            counter-reset: section;
        }
        .section-number::before {
            counter-increment: section;
            content: counter(section);
        }
        .required-field::after {
            content: "*";
            color: #e53e3e;
            margin-left: 4px;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <!-- Header -->
    <header class="chimera-gradient text-white p-6 shadow-md">
        <div class="container mx-auto flex flex-col md:flex-row items-center justify-between">
            <div class="flex items-center mb-4 md:mb-0">
                <i class="fas fa-brain text-4xl mr-3"></i>
                <div>
                    <h1 class="text-3xl font-bold">Chimera v2.0</h1>
                    <p class="text-sm opacity-80">Brain-Controlled Exoskeleton Platform</p>
                </div>
            </div>
            <div>
                <h2 class="text-2xl font-semibold flex items-center">
                    <i class="fas fa-bug mr-2"></i>
                    Bug Report Form
                </h2>
            </div>
        </div>
    </header>

    <!-- Main Form Container -->
    <main class="container mx-auto px-4 py-8 max-w-5xl">
        <!-- Introduction Section -->
        <div class="bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="flex items-start">
                <div class="bg-blue-100 p-3 rounded-full mr-4">
                    <i class="fas fa-info-circle text-blue-600 text-xl"></i>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-blue-800 mb-2">Before Submitting a Bug Report</h3>
                    <p class="mb-4">Please ensure you have completed these steps before filing a new report:</p>
                    <ul class="list-disc ml-5 space-y-1 text-gray-700">
                        <li>Search existing issues to avoid duplicates</li>
                        <li>Update to the latest version to verify the bug still exists</li>
                        <li>Read the documentation and FAQs for known solutions</li>
                        <li>Collect all relevant logs, configurations, and screenshots</li>
                        <li>Test with minimal configuration to isolate the issue</li>
                    </ul>
                    <div class="mt-4 text-sm bg-yellow-50 border-l-4 border-yellow-400 p-4">
                        <p class="font-semibold flex items-center"><i class="fas fa-exclamation-triangle text-yellow-500 mr-2"></i> Important</p>
                        <p>Fields marked with an asterisk (*) are required. Please provide as much detail as possible to help us investigate and resolve your issue efficiently.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Bug Metadata Section -->
        <div class="section-card bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="flex items-center mb-4">
                <span class="section-number bg-purple-700 text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 font-bold text-sm"></span>
                <h2 class="text-xl font-bold text-gray-800">Bug Metadata</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1 required-field">Bug Title</label>
                    <input type="text" placeholder="Concise summary of the issue" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                    <p class="mt-1 text-xs text-gray-500">Keep it clear and specific (e.g., "EEG Signal Processing Fails When Using 64-Channel Montage")</p>
                </div>
                
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Related Issues</label>
                    <input type="text" placeholder="e.g., #123, #456" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                    <p class="mt-1 text-xs text-gray-500">Link any related or duplicate issues if applicable</p>
                </div>
                
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1 required-field">Bug Type</label>
                    <select class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                        <option value="">Select Bug Type</option>
                        <option value="functional">Functional Error</option>
                        <option value="performance">Performance Issue</option>
                        <option value="ui">UI/UX Problem</option>
                        <option value="compatibility">Compatibility Issue</option>
                        <option value="security">Security Vulnerability</option>
                        <option value="crash">System Crash</option>
                        <option value="data">Data Processing Error</option>
                        <option value="documentation">Documentation Error</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1 required-field">Priority</label>
                    <select class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                        <option value="">Select Priority</option>
                        <option value="critical">Critical - System Unusable</option>
                        <option value="high">High - Major Feature Impacted</option>
                        <option value="medium">Medium - Partial Functionality Affected</option>
                        <option value="low">Low - Minor Issue</option>
                        <option value="trivial">Trivial - Cosmetic Problem</option>
                    </select>
                </div>
            </div>
            
            <div class="mt-6">
                <label class="block text-sm font-medium text-gray-700 mb-1">Tags</label>
                <input type="text" placeholder="e.g., signal-processing, hardware, calibration" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                <p class="mt-1 text-xs text-gray-500">Add relevant tags to categorize the issue (comma-separated)</p>
            </div>
        </div>

        <!-- Bug Description Section -->
        <div class="section-card bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="flex items-center mb-4">
                <span class="section-number bg-purple-700 text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 font-bold text-sm"></span>
                <h2 class="text-xl font-bold text-gray-800">Bug Description</h2>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-1 required-field">Detailed Description</label>
                <textarea rows="6" placeholder="Provide a clear and detailed description of the bug..." class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500"></textarea>
                <p class="mt-1 text-xs text-gray-500">Describe the issue thoroughly, including context and conditions when it occurs</p>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-1 required-field">Steps to Reproduce</label>
                <div class="bg-gray-50 p-4 rounded-md border border-gray-200">
                    <div class="reproduction-steps">
                        <div class="flex items-start mb-3">
                            <span class="bg-purple-100 text-purple-700 rounded-full w-6 h-6 flex items-center justify-center mr-2 mt-1 flex-shrink-0 font-medium">1</span>
                            <input type="text" placeholder="First step..." class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                        </div>
                        <div class="flex items-start mb-3">
                            <span class="bg-purple-100 text-purple-700 rounded-full w-6 h-6 flex items-center justify-center mr-2 mt-1 flex-shrink-0 font-medium">2</span>
                            <input type="text" placeholder="Second step..." class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                        </div>
                        <div class="flex items-start mb-3">
                            <span class="bg-purple-100 text-purple-700 rounded-full w-6 h-6 flex items-center justify-center mr-2 mt-1 flex-shrink-0 font-medium">3</span>
                            <input type="text" placeholder="Third step..." class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                        </div>
                    </div>
                    <button type="button" class="mt-2 flex items-center text-sm text-purple-600 hover:text-purple-800">
                        <i class="fas fa-plus-circle mr-1"></i> Add More Steps
                    </button>
                </div>
                <p class="mt-1 text-xs text-gray-500">Provide a step-by-step guide to reproduce the issue consistently</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1 required-field">Expected Behavior</label>
                    <textarea rows="4" placeholder="What should happen..." class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500"></textarea>
                    <p class="mt-1 text-xs text-gray-500">Describe what should happen when steps are followed</p>
                </div>
                
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1 required-field">Actual Behavior</label>
                    <textarea rows="4" placeholder="What actually happens..." class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500"></textarea>
                    <p class="mt-1 text-xs text-gray-500">Describe what actually happens instead</p>
                </div>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Frequency</label>
                <div class="flex flex-wrap gap-4">
                    <label class="inline-flex items-center">
                        <input type="radio" name="frequency" value="always" class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300">
                        <span class="ml-2 text-sm">Always</span>
                    </label>
                    <label class="inline-flex items-center">
                        <input type="radio" name="frequency" value="often" class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300">
                        <span class="ml-2 text-sm">Often</span>
                    </label>
                    <label class="inline-flex items-center">
                        <input type="radio" name="frequency" value="sometimes" class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300">
                        <span class="ml-2 text-sm">Sometimes</span>
                    </label>
                    <label class="inline-flex items-center">
                        <input type="radio" name="frequency" value="rarely" class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300">
                        <span class="ml-2 text-sm">Rarely</span>
                    </label>
                    <label class="inline-flex items-center">
                        <input type="radio" name="frequency" value="once" class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300">
                        <span class="ml-2 text-sm">Once</span>
                    </label>
                </div>
                <p class="mt-1 text-xs text-gray-500">How often does the bug occur when the steps are followed?</p>
            </div>
        </div>

        <!-- Environment Details -->
        <div class="section-card bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="flex items-center mb-4">
                <span class="section-number bg-purple-700 text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 font-bold text-sm"></span>
                <h2 class="text-xl font-bold text-gray-800">Environment Details</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1 required-field">Chimera Version</label>
                    <input type="text" placeholder="e.g., v2.0.1" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                </div>
                
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1 required-field">Python Version</label>
                    <input type="text" placeholder="e.g., 3.9.7" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                </div>
                
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1 required-field">Operating System</label>
                    <input type="text" placeholder="e.g., Ubuntu 22.04, Windows 11" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                </div>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-2">Development Environment</label>
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div>
                        <label class="block text-xs text-gray-600 mb-1">Using Poetry</label>
                        <select class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                            <option value="yes">Yes</option>
                            <option value="no">No</option>
                        </select>
                    </div>
                    
                    <div>
                        <label class="block text-xs text-gray-600 mb-1">Poetry Version</label>
                        <input type="text" placeholder="e.g., 1.2.0" class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                    </div>
                    
                    <div>
                        <label class="block text-xs text-gray-600 mb-1">Virtual Environment</label>
                        <select class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                            <option value="poetry">Poetry</option>
                            <option value="venv">venv</option>
                            <option value="conda">conda</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    
                    <div>
                        <label class="block text-xs text-gray-600 mb-1">DVC Enabled</label>
                        <select class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                            <option value="yes">Yes</option>
                            <option value="no">No</option>
                        </select>
                    </div>
                </div>
            </div>
            
            <div class="mb-6">
                <h3 class="text-sm font-medium text-gray-700 mb-2">Hardware Details (if relevant)</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs text-gray-600 mb-1">CPU</label>
                        <input type="text" placeholder="e.g., Intel i7-11700K, 8 cores" class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                    </div>
                    
                    <div>
                        <label class="block text-xs text-gray-600 mb-1">RAM</label>
                        <input type="text" placeholder="e.g., 32GB DDR4" class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                    </div>
                    
                    <div>
                        <label class="block text-xs text-gray-600 mb-1">GPU (if applicable)</label>
                        <input type="text" placeholder="e.g., NVIDIA RTX 3080, 10GB VRAM" class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                    </div>
                    
                    <div>
                        <label class="block text-xs text-gray-600 mb-1">EEG Device Model</label>
                        <input type="text" placeholder="e.g., Emotiv EPOC X" class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                    </div>
                </div>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Additional Environment Details</label>
                <textarea rows="3" placeholder="Any other relevant environment details..." class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500"></textarea>
                <p class="mt-1 text-xs text-gray-500">Include any other specific environment details that might be relevant</p>
            </div>
        </div>

        <!-- Technical Details -->
        <div class="section-card bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="flex items-center mb-4">
                <span class="section-number bg-purple-700 text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 font-bold text-sm"></span>
                <h2 class="text-xl font-bold text-gray-800">Technical Details</h2>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-1">Error Messages & Stack Traces</label>
                <div class="rounded-md border border-gray-300 overflow-hidden">
                    <div class="bg-gray-100 px-4 py-2 text-sm font-medium border-b border-gray-300 flex justify-between items-center">
                        <span>Error Output</span>
                        <span class="text-xs text-gray-500">Format: Plain Text</span>
                    </div>
                    <textarea rows="8" placeholder="Paste error messages and stack traces here..." class="w-full px-4 py-3 border-0 focus:ring-0 font-mono text-sm"></textarea>
                </div>
                <p class="mt-1 text-xs text-gray-500">Include complete error messages and stack traces if available</p>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-1">Configuration Files</label>
                <div class="rounded-md border border-gray-300 overflow-hidden">
                    <div class="bg-gray-100 px-4 py-2 text-sm font-medium border-b border-gray-300 flex justify-between items-center">
                        <span>Configuration (YAML/JSON/etc.)</span>
                        <div>
                            <select class="text-xs border border-gray-300 rounded px-2 py-1">
                                <option value="yaml">YAML</option>
                                <option value="json">JSON</option>
                                <option value="toml">TOML</option>
                                <option value="python">Python</option>
                                <option value="plain">Plain Text</option>
                            </select>
                        </div>
                    </div>
                    <textarea rows="6" placeholder="Paste relevant configuration here..." class="w-full px-4 py-3 border-0 focus:ring-0 font-mono text-sm"></textarea>
                </div>
                <p class="mt-1 text-xs text-gray-500">Include relevant Hydra configurations or other configuration files</p>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-1">Log Output</label>
                <div class="rounded-md border border-gray-300 overflow-hidden">
                    <div class="bg-gray-100 px-4 py-2 text-sm font-medium border-b border-gray-300 flex justify-between items-center">
                        <span>Log Content</span>
                        <span class="text-xs text-gray-500">Format: Plain Text</span>
                    </div>
                    <textarea rows="6" placeholder="Paste relevant logs here..." class="w-full px-4 py-3 border-0 focus:ring-0 font-mono text-sm"></textarea>
                </div>
                <p class="mt-1 text-xs text-gray-500">Include relevant log output (please remove any sensitive information)</p>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Code Snippets</label>
                <div class="rounded-md border border-gray-300 overflow-hidden">
                    <div class="bg-gray-100 px-4 py-2 text-sm font-medium border-b border-gray-300 flex justify-between items-center">
                        <span>Code</span>
                        <div>
                            <select class="text-xs border border-gray-300 rounded px-2 py-1">
                                <option value="python">Python</option>
                                <option value="bash">Bash</option>
                                <option value="html">HTML</option>
                                <option value="javascript">JavaScript</option>
                                <option value="plain">Plain Text</option>
                            </select>
                        </div>
                    </div>
                    <textarea rows="6" placeholder="Paste relevant code snippets here..." class="w-full px-4 py-3 border-0 focus:ring-0 font-mono text-sm"></textarea>
                </div>
                <p class="mt-1 text-xs text-gray-500">Include code snippets that help reproduce or understand the issue</p>
            </div>
        </div>

        <!-- Visual Evidence -->
        <div class="section-card bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="flex items-center mb-4">
                <span class="section-number bg-purple-700 text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 font-bold text-sm"></span>
                <h2 class="text-xl font-bold text-gray-800">Visual Evidence</h2>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-2">Screenshots / Images</label>
                <div class="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center">
                    <div class="mb-3">
                        <i class="fas fa-cloud-upload-alt text-3xl text-gray-400"></i>
                    </div>
                    <div class="mb-3">
                        <span class="text-sm text-gray-600">Drag and drop image files here, or</span>
                    </div>
                    <div>
                        <button type="button" class="bg-purple-600 hover:bg-purple-700 text-white font-medium py-2 px-4 rounded-md transition-colors">
                            Browse Files
                        </button>
                    </div>
                    <div class="mt-2">
                        <span class="text-xs text-gray-500">Support for PNG, JPG, GIF up to 10MB each</span>
                    </div>
                </div>
                <div class="mt-3 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
                    <!-- Image preview placeholders would appear here -->
                </div>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Videos / Screen Recordings</label>
                <div class="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center">
                    <div class="mb-3">
                        <i class="fas fa-film text-3xl text-gray-400"></i>
                    </div>
                    <div class="mb-3">
                        <span class="text-sm text-gray-600">Drag and drop video files here, or</span>
                    </div>
                    <div>
                        <button type="button" class="bg-purple-600 hover:bg-purple-700 text-white font-medium py-2 px-4 rounded-md transition-colors">
                            Browse Files
                        </button>
                    </div>
                    <div class="mt-2">
                        <span class="text-xs text-gray-500">Support for MP4, WebM up to 100MB each</span>
                    </div>
                </div>
                <div class="mt-3">
                    <!-- Video preview placeholders would appear here -->
                </div>
            </div>
        </div>

        <!-- Impact & Context -->
        <div class="section-card bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="flex items-center mb-4">
                <span class="section-number bg-purple-700 text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 font-bold text-sm"></span>
                <h2 class="text-xl font-bold text-gray-800">Impact & Context</h2>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-1">Business Impact</label>
                <textarea rows="3" placeholder="Describe how this bug impacts users, operations, or research..." class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500"></textarea>
                <p class="mt-1 text-xs text-gray-500">Explain the real-world consequences of this bug</p>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-1">User Scope</label>
                <div class="flex flex-wrap gap-4">
                    <label class="inline-flex items-center">
                        <input type="radio" name="user-scope" value="all" class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300">
                        <span class="ml-2 text-sm">All Users</span>
                    </label>
                    <label class="inline-flex items-center">
                        <input type="radio" name="user-scope" value="specific" class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300">
                        <span class="ml-2 text-sm">Specific User Group</span>
                    </label>
                    <label class="inline-flex items-center">
                        <input type="radio" name="user-scope" value="edge" class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300">
                        <span class="ml-2 text-sm">Edge Case</span>
                    </label>
                </div>
                <div class="mt-2" id="specific-user-details" style="display: none;">
                    <label class="block text-xs text-gray-600 mb-1">Specify User Group</label>
                    <input type="text" placeholder="e.g., researchers, clinical users, etc." class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                </div>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-1">Workaround Available?</label>
                <div class="flex items-center">
                    <label class="inline-flex items-center mr-6">
                        <input type="radio" name="workaround" value="yes" class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300">
                        <span class="ml-2 text-sm">Yes</span>
                    </label>
                    <label class="inline-flex items-center">
                        <input type="radio" name="workaround" value="no" class="h-4 w-4 text-purple-600 focus:ring-purple-500 border-gray-300">
                        <span class="ml-2 text-sm">No</span>
                    </label>
                </div>
                <div class="mt-2" id="workaround-details" style="display: none;">
                    <label class="block text-xs text-gray-600 mb-1">Describe Workaround</label>
                    <textarea rows="3" placeholder="Provide details on how to work around this issue..." class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500"></textarea>
                </div>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Regression Information</label>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs text-gray-600 mb-1">Last Known Working Version</label>
                        <input type="text" placeholder="e.g., v1.9.3" class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                    </div>
                    <div>
                        <label class="block text-xs text-gray-600 mb-1">First Broken Version</label>
                        <input type="text" placeholder="e.g., v2.0.0" class="w-full px-3 py-1 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500">
                    </div>
                </div>
            </div>
        </div>

        <!-- Proposed Solution -->
        <div class="section-card bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="flex items-center mb-4">
                <span class="section-number bg-purple-700 text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 font-bold text-sm"></span>
                <h2 class="text-xl font-bold text-gray-800">Proposed Solution</h2>
            </div>
            
            <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-1">Possible Solution</label>
                <textarea rows="4" placeholder="If you have insights on what might fix this issue..." class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500"></textarea>
                <p class="mt-1 text-xs text-gray-500">Share any thoughts on how this bug might be resolved</p>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Suggested Test Cases</label>
                <textarea rows="4" placeholder="If applicable, suggest tests that would verify a fix..." class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500"></textarea>
                <p class="mt-1 text-xs text-gray-500">Suggest how a fix for this issue could be tested and verified</p>
            </div>
        </div>

        <!-- Additional Information -->
        <div class="section-card bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="flex items-center mb-4">
                <span class="section-number bg-purple-700 text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 font-bold text-sm"></span>
                <h2 class="text-xl font-bold text-gray-800">Additional Information</h2>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Any Other Context</label>
                <textarea rows="4" placeholder="Any other information that might be relevant..." class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500"></textarea>
                <p class="mt-1 text-xs text-gray-500">Include any other information that might help diagnose or fix the issue</p>
            </div>
        </div>

        <!-- Submission Checklist -->
        <div class="section-card bg-white rounded-lg shadow-sm p-6 mb-8">
            <div class="flex items-center mb-4">
                <span class="section-number bg-purple-700 text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 font-bold text-sm"></span>
                <h2 class="text-xl font-bold text-gray-800">Submission Checklist</h2>
            </div>
            
            <p class="text-sm text-gray-600 mb-4">Please confirm that you have completed the following before submitting:</p>
            
            <div class="space-y-3">
                <label class="flex items-start">
                    <input type="checkbox" class="h-5 w-5 text-purple-600 focus:ring-purple-500 border-gray-300 rounded mt-0.5">
                    <span class="ml-2 text-sm">I have searched existing issues to ensure this bug hasn't already been reported</span>
                </label>
                
                <label class="flex items-start">
                    <input type="checkbox" class="h-5 w-5 text-purple-600 focus:ring-purple-500 border-gray-300 rounded mt-0.5">
                    <span class="ml-2 text-sm">I have included all the information requested in this form to the best of my ability</span>
                </label>
                
                <label class="flex items-start">
                    <input type="checkbox" class="h-5 w-5 text-purple-600 focus:ring-purple-500 border-gray-300 rounded mt-0.5">
                    <span class="ml-2 text-sm">I have verified the issue still occurs in the latest version of Chimera</span>
                </label>
                
                <label class="flex items-start">
                    <input type="checkbox" class="h-5 w-5 text-purple-600 focus:ring-purple-500 border-gray-300 rounded mt-0.5">
                    <span class="ml-2 text-sm">I have tested with minimal/default configuration to ensure the issue isn't specific to my setup</span>
                </label>
                
                <label class="flex items-start">
                    <input type="checkbox" class="h-5 w-5 text-purple-600 focus:ring-purple-500 border-gray-300 rounded mt-0.5">
                    <span class="ml-2 text-sm">I have run linting and formatting tools to verify this isn't a code style issue</span>
                </label>
                
                <label class="flex items-start">
                    <input type="checkbox" class="h-5 w-5 text-purple-600 focus:ring-purple-500 border-gray-300 rounded mt-0.5">
                    <span class="ml-2 text-sm">I have checked logs for confidential information before sharing</span>
                </label>
                
                <label class="flex items-start">
                    <input type="checkbox" class="h-5 w-5 text-purple-600 focus:ring-purple-500 border-gray-300 rounded mt-0.5">
                    <span class="ml-2 text-sm">I understand my issue will be closed if I don't provide requested information</span>
                </label>
            </div>
        </div>

        <!-- Submit Button -->
        <div class="flex justify-end mb-8">
            <button type="submit" class="bg-purple-600 hover:bg-purple-700 text-white font-medium py-3 px-6 rounded-md transition-colors flex items-center">
                <i class="fas fa-paper-plane mr-2"></i>
                Submit Bug Report
            </button>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-8">
        <div class="container mx-auto px-4 text-center">
            <div class="mb-4">
                <i class="fas fa-brain text-3xl"></i>
            </div>
            <h3 class="text-xl font-bold mb-2">Chimera v2.0</h3>
            <p class="text-gray-400 mb-4">Brain-Controlled Exoskeleton Platform</p>
            <div class="flex justify-center space-x-4 mb-6">
                <a href="#" class="text-gray-400 hover:text-white">
                    <i class="fab fa-github text-xl"></i>
                </a>
                <a href="#" class="text-gray-400 hover:text-white">
                    <i class="fab fa-slack text-xl"></i>
                </a>
                <a href="#" class="text-gray-400 hover:text-white">
                    <i class="fas fa-book text-xl"></i>
                </a>
            </div>
            <p class="text-sm text-gray-500">© 2025 Chimera Project. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Show/hide specific user group details
        const userScopeRadios = document.querySelectorAll('input[name="user-scope"]');
        const specificUserDetails = document.getElementById('specific-user-details');
        
        userScopeRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                if (this.value === 'specific') {
                    specificUserDetails.style.display = 'block';
                } else {
                    specificUserDetails.style.display = 'none';
                }
            });
        });
        
        // Show/hide workaround details
        const workaroundRadios = document.querySelectorAll('input[name="workaround"]');
        const workaroundDetails = document.getElementById('workaround-details');
        
        workaroundRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                if (this.value === 'yes') {
                    workaroundDetails.style.display = 'block';
                } else {
                    workaroundDetails.style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>
